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
![Image](images/model.png)

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







