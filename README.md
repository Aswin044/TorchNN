# Torch Neural Network - MNIST Digit Classifier

This project demonstrates a basic convolutional neural network (CNN) built using PyTorch to classify handwritten digits from the MNIST dataset.

## 📌 Project Overview

- Loads the MNIST dataset using `torchvision.datasets`
- Builds a CNN with three convolutional layers
- Trains the model using Adam optimizer and Cross Entropy Loss
- Saves and reloads the trained model
- Predicts digit class for a custom image

## 🧠 Model Architecture

The CNN consists of the following layers:

1. `Conv2D(1 → 32)` with ReLU  
2. `Conv2D(32 → 64)` with ReLU  
3. `Conv2D(64 → 64)` with ReLU  
4. Flatten  
5. Linear layer mapping to 10 output classes (digits 0–9)

Input image dimensions are 28x28 grayscale (as in MNIST).

## 🛠️ Installation & Requirements

Ensure you have the following installed:

```bash
pip install torch torchvision pillow
