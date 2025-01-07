## PyTorch Tensor Types and Use Cases And Data types

### 1. Scalar Tensor
```python
scalar = torch.tensor(5)  # Single value
# Useful for: Loss values, single predictions
```

### 2. Vector Tensor
```python
vector = torch.tensor([1, 2, 3, 4])  # 1D array
# Useful for: Feature vectors, embeddings, model weights
```

### 3. Matrix Tensor
```python
matrix = torch.tensor([[1, 2], [3, 4]])  # 2D array
# Useful for: Image pixel data, linear algebra operations
```

### 4. 3D Tensor
```python
tensor_3d = torch.randn(3, 64, 64)  # Color images, video frames
# Useful for: Image processing, video analysis, time series
```

### 5. 4D Tensor
```python
tensor_4d = torch.randn(10, 3, 64, 64)  # Batch of color images
# Useful for: Batch processing in deep learning
```

### Data Types
```python
# Common PyTorch data types
torch.float32  # Default, neural networks
torch.float16  # Mixed precision training
torch.int64    # Integer operations
torch.bool     # Boolean masks
```


