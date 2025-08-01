# -*- coding: utf-8 -*-
"""TorchNeuralNetwork.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HV9JTq71RTHI-XLleNfIU8jZXnjWp5r8
"""

import torch
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

train = datasets.MNIST(root = "data", download = True, train = True, transform = ToTensor())  #Pytorch has a built in dataset for loading MNIST which is handwritten numbers
dataset = DataLoader(train,32) # trian is the name of the dataset to load from and 32 is the batch size
# ToTensor() converts each image to PIL format which is used fro training purpose

#@title Neural Network

#1,28,28 0-9 classes
class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, (3, 3)),  #MNIST images are grayscale 1 input channel and 32 output channels 3x3 kernel size
            nn.ReLU(),                 #28x28 - 26x26 no padding
            nn.Conv2d(32, 64, (3, 3)), # 64 output channels
            nn.ReLU(),                 # 26x26 - 24x24
            nn.Conv2d(64, 64, (3, 3)),
            nn.ReLU(),                 # 24x24 - 22x22
            nn.Flatten(),              # convert fro 3d to 2d
            nn.Linear(64 * (28 - 6) * (28 - 6), 10) # to convert into 22*22 we do this as our final spatial dimension
        )
    def forward(self,x):
      return self.model(x)

clf = ImageClassifier() #ImageClassificatioModel
opt = Adam(clf.parameters(), lr=1e-3) #
loss_fn = nn.CrossEntropyLoss()

if __name__ == "__main__":
  for epoch in range(10):  # we train for 10 epochs
    for batch in dataset:
      X,y = batch
      yhat = clf(X)
      loss = loss_fn(yhat,y)

      opt.zero_grad()
      loss.backward()
      opt.step()

    print(f"Epoch:{epoch} loss is {loss.item()}")
  with open("model_state.pt", "wb") as f:
    save(clf.state_dict(), f)

  with open("model_state.pt", "rb") as f:
    clf.load_state_dict(load(f))

from PIL import Image
img = Image.open('img_3.jpg')
img_tensor = ToTensor()(img).unsqueeze(0)

print(torch.argmax(clf(img_tensor)))