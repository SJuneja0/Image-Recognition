# Run this script: python src/image_processor.py
from mnist import MNIST
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import random

class ImageProcessor:

    # Shuffle determines whether or not the train loader dataset is shuffled (good to turn off when testing show_select_image)
    def __init__(self, shuffle=True):
        print("Running")
        # Load training and test datasets
        self.train_dataset = datasets.MNIST(root='dataset', train=True, download=True, transform=transforms.ToTensor())
        self.test_dataset = datasets.MNIST(root='dataset', train=False, download=True, transform=transforms.ToTensor())

        # Create data loaders (batching and shuffling)
        self.train_loader = DataLoader(dataset=self.train_dataset, batch_size=64, shuffle=shuffle)
        self.test_loader = DataLoader(dataset=self.test_dataset, batch_size=64, shuffle=False)

    def show_rand_img(self):
        # Pick a random image and label from the torchvision dataset
        images, labels = next(iter(self.train_loader))
        index = random.randint(0, len(images) - 1)


        print(images[index].squeeze())
        print("\n \n")
        print(images[index])
        print(labels[index])
        plt.imshow(images[index].squeeze(), cmap="gray")
        plt.title(f"Label: {labels[index].item()}")
        plt.show()

    def show_select_img(self, index):
        images, labels = next(iter(self.train_loader))

        print(images[index].squeeze())
        print("\n \n")
        print(images[index])
        print(labels[index])
        plt.imshow(images[index].squeeze(), cmap="gray")
        plt.title(f"Label: {labels[index].item()}")
        plt.show()

    def show_range_imgs(self, range):
        images, labels = next(iter(self.train_loader))

        for index in range:
            print(images[index].squeeze())
            print("\n \n")
            print(images[index])
            print(labels[index])
            plt.imshow(images[index].squeeze(), cmap="gray")
            plt.title(f"Label: {labels[index].item()}")
            plt.show()


# Rough testing
IP = ImageProcessor()
# IP.show_rand_img()
IP = ImageProcessor(shuffle=False)
IP.show_select_img(0)
IP.show_range_imgs([0, 1, 2])
