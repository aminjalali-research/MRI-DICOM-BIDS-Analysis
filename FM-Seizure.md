# Function 1: Masking the tensor to pretrain the model
- This function takes a 3D tensor (`data`), selects certain "channels" (by default [1, 2, 3]), and sets all their values to zero (i.e., masks them). `data` is a PyTorch tensor with shape (batch_size, num_channels, length).

``` python
import torch

# Create a dummy tensor of shape (2, 5, 4)
# (batch_size=2, num_channels=5, length=4)
data = torch.arange(2*5*4).float().reshape(2, 5, 4)
print("Original data:")
print(data)

def mask_channels(data, channels=[1, 2, 3]):
    data[:, channels, :] = 0
    return data

# Mask channels 1, 2, 3
masked = mask_channels(data.clone(), channels=[1,2,3])
print("\nMasked data:")
print(masked)
```

The original tensor has values from 0 to 39 arranged in shape (2, 5, 4). After calling mask_channels on channels 1, 2, and 3, all those channels become zeros for both batches.  

```python
Original data:
tensor([[[ 0.,  1.,  2.,  3.],
         [ 4.,  5.,  6.,  7.],
         [ 8.,  9., 10., 11.],
         [12., 13., 14., 15.],
         [16., 17., 18., 19.]],

        [[20., 21., 22., 23.],
         [24., 25., 26., 27.],
         [28., 29., 30., 31.],
         [32., 33., 34., 35.],
         [36., 37., 38., 39.]]])

Masked data:
tensor([[[ 0.,  1.,  2.,  3.],
         [ 0.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  0.],
         [16., 17., 18., 19.]],

        [[20., 21., 22., 23.],
         [ 0.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  0.],
         [ 0.,  0.,  0.,  0.],
         [36., 37., 38., 39.]]])
```
# Function 2: Masks a percentage of the time axis
- Standardization: By first converting the Python input to a NumPy array `(np.array(data))` and then to PyTorch tensors `torch.from_numpy(np.array(data))`, we ensure that no matter how it started, it ends up as a PyTorch tensor—ready for downstream processing.
- Randomly selects a contiguous range of time steps to mask (set to zero), based on `mask_percentage`.

<p align="center">
  <img src="images/Model.png" width="500" height="200"/>
</p>


```python
def collate_mask_time(data, mask_percentage):
    data = torch.from_numpy(np.array(data)) / 100   # Normalize (divided by 100)
    data_len = data.shape[-1]                      # Number of time steps (4)
    mask_start_idx = random.randint(0, int(data_len * (1-mask_percentage)))
    mask_end_idx = mask_start_idx + int(data_len*mask_percentage)
    masked_data = data.clone()
    masked_data[:, :, mask_start_idx:mask_end_idx] = 0
    return masked_data, data, [mask_start_idx, mask_end_idx]

# Fix the random seed for reproducibility (optional)
random.seed(42)

masked, normalized, [start, end] = collate_mask_time(data.clone(), 0.5)

print("\nNormalized data (divided by 100):\n", normalized)
print(f"\nMasking indices: {start} to {end} (mask_percentage=0.5)")

print("\nMasked data:\n", masked)
```
- For a 50% mask, the output is as below:
```python
tensor([[[0.00, 0.00, 0.02, 0.03],
         [0.00, 0.00, 0.06, 0.07],
         [0.00, 0.00, 0.10, 0.11],
         [0.00, 0.00, 0.14, 0.15],
         [0.00, 0.00, 0.18, 0.19]],

        [[0.00, 0.00, 0.22, 0.23],
         [0.00, 0.00, 0.26, 0.27],
         [0.00, 0.00, 0.30, 0.31],
         [0.00, 0.00, 0.34, 0.35],
         [0.00, 0.00, 0.38, 0.39]]])
```

# Read one HDF5 file, slicing the EEG data into overlapping windows
```python
import h5py         # For reading HDF5 data files
import bisect       # For fast index searching (binary search)
from pathlib import Path   # For safe file path operations
from typing import List    # For type annotations
from torch.utils.data import Dataset  # Base class for PyTorch datasets

list_path = List[Path]    # Type alias: list of Path objects
```

Class Declaration which inherits from PyTorch's `Dataset`, so you can use it in DataLoader.


```python
class SingleShockDataset(Dataset):
    # Define the constructor
    def __init__(self, file_path: Path, window_size: int=200, stride_size: int=1, start_percentage: float=0, end_percentage: float=1):
        self.__file_path = file_path
        self.__window_size = window_size      # Length of each sample window (e.g., 200 timepoints)
        self.__stride_size = stride_size      # Step between consecutive windows (e.g., 1 = highly overlapping)
        self.__start_percentage = start_percentage   # For subsampling data from the start
        self.__end_percentage = end_percentage       # For subsampling data to the end

        self.__file = None
        self.__length = None
        self.__feature_size = None

        self.__subjects = []         # List of all subjects in this file
        self.__global_idxes = []     # List of global start indices for each subject's data in the dataset
        self.__local_idxes = []      # List of local start indices (relative to each subject)

        self.__init_dataset()        # Actually load file and prepare index bookkeeping

    # Open file for reading (h5py.File) and list all subjects (e.g., subject_001, subject_002).
    # `-> None` means: This function does not return anything. `-> int`	Returns an integer. `-> List[str]`	Returns a list of strings.
    def __init_dataset(self) -> None:          
        self.__file = h5py.File(str(self.__file_path), 'r')
        self.__subjects = [i for i in self.__file]

    global_idx = 0
    for subject in self.__subjects:
        self.__global_idxes.append(global_idx) # Store the running total of samples so far

        subject_len = self.__file[subject]['eeg'].shape[1]  # Number of time points in this subject
        total_sample_num = (subject_len-self.__window_size) // self.__stride_size + 1

        # Calculate how many windows you can get for each subject, given the window and stride.
        # E.g., if you have 1000 points, window=200, stride=100 → (1000-200)//100+1 = 9 samples.

        start_idx = int(total_sample_num * self.__start_percentage) * self.__stride_size 
        end_idx = int(total_sample_num * self.__end_percentage - 1) * self.__stride_size

        self.__local_idxes.append(start_idx) #Store starting index for this subject and increment total global count.
        global_idx += (end_idx - start_idx) // self.__stride_size + 1

        self.__length = global_idx  # Total number of windows in this dataset

        self.__feature_size = [i for i in self.__file[self.__subjects[0]]['eeg'].shape]
        self.__feature_size[1] = self.__window_size  # Set feature size to match window
```

# Properties and Magic Methods
```python
@property
def feature_size(self):
    return self.__feature_size

def __len__(self):   # Length (number of samples/windows)
    return self.__length

def __getitem__(self, idx: int):     # Find which subject this sample comes from (bisect for fast search). Calculate local window start for that subject.
                                     # Return EEG data: all channels, windowed timepoints.
    subject_idx = bisect.bisect(self.__global_idxes, idx) - 1
    item_start_idx = (idx - self.__global_idxes[subject_idx]) * self.__stride_size + self.__local_idxes[subject_idx]
    return self.__file[self.__subjects[subject_idx]]['eeg'][:, item_start_idx:item_start_idx+self.__window_size]

def free(self) -> None:  # Free resources (close file)
    if self.__file:
        self.__file.close()
        self.__file = None

def get_ch_names(self):   # Get Channel Names
    return self.__file[self.__subjects[0]]['eeg'].attrs['chOrder']

```

# Combine multiple files into one big dataset 
This makes it easy to load, slice, and batch EEG data for neural network training. Makes a list of SingleShockDataset (one per file).
Calculates cumulative sample indices for efficient lookup. Sets overall dataset length and shape.

```python
def __init_dataset(self) -> None:
    self.__datasets = [SingleShockDataset(file_path, self.__window_size, self.__stride_size, self.__start_percentage, self.__end_percentage) for file_path in self.__file_paths]
    
    dataset_idx = 0
    for dataset in self.__datasets:
        self.__dataset_idxes.append(dataset_idx)
        dataset_idx += len(dataset)
    self.__length = dataset_idx

    self.__feature_size = self.__datasets[0].feature_size
```

# "Properties" and "Magic Methods" in Python
"Properties" make methods in your class look like normal variables and read-only to users of the class.
For example, `.area` looks like a variable but is actually computed when accessed.
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        # Looks like an attribute, but is calculated on-the-fly
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # 78.5
```

Magic Methods (also called dunder methods for “double underscore,” like __len__, __getitem__, etc.) make objects behave like built-in types (lists, dicts). To allow objects to be used with Python’s special syntax (len(obj), obj[2], str(obj), etc.)

Common Magic Methods:
- `__len__(self)` → For len(obj)
- `__getitem__(self, index)` → For obj[index]
- `__setitem__(self, index, value)` → For assignment like obj[index] = value
- `__str__(self)` → For str(obj) or print(obj)
- `__init__(self, ...)` → The constructor! It lets you set up initial values (attributes) for your object.

The `MyList` custom class acts like a list! Without `__init__`, every object would be identical or incomplete. 
The objects won’t have any custom attributes unless you add them after creation.
`self` refers to the object being created.

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

lst = MyList([1, 2, 3])
print(len(lst))    # 3
print(lst[1])      # 2
```













