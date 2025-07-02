# Masking the tensor to pretrain the model
- This function takes a 3D tensor (data), selects certain "channels" (by default [1, 2, 3]), and sets all their values to zero (i.e., masks them).
- data is a PyTorch tensor with shape (batch_size, num_channels, length).

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
# Function 2: collate_mask_time(data, mask_percentage)
