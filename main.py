import torch
import torchvision
import sys

print(sys.version)
print(f"PyTorch version: {torch.__version__}")
print(f"Torchvision version: {torchvision.__version__}")

x =  torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y= torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(x.device)
print(x.dtype)
print(x.matmul(y))

print(f"Is CUDA available? {torch.cuda.is_available()}")
