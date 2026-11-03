from torchvision import datasets
from torchvision.transforms import v2
import matplotlib.pyplot as plt
import torch

training_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

test_data = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

print(len(training_data))
print(len(test_data))

image,label = training_data[0]
print(image.shape)
print(image.dtype)
print(image.max())


fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(9,9))
for i, ax in enumerate(axes.flat):
    image, label = training_data[i]
    ax.imshow(image.squeeze(), cmap="gray")
    ax.set_title(f"Label: {label}")
    ax.axis("off")
plt.show()