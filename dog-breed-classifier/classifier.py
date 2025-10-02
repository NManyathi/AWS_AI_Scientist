"""
Image Classification Module using Pretrained PyTorch Models

This script demonstrates the use of pretrained deep learning models
(ResNet18, AlexNet, VGG16) for image classification tasks. It provides
a reusable function `classifier` that can classify any given image into
one of 1000 ImageNet classes. 

Key Highlights:
- Uses standard preprocessing pipelines (resize, crop, normalization).
- Supports multiple pretrained models for flexibility and comparison.
- Handles PyTorch version differences in Variable API for backward compatibility.
- Evaluation mode ensures inference-only operation without affecting model weights.
- Designed for clarity, maintainability, and professional standards suitable for
  portfolios, client demonstrations, and employment projects.
"""

import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load pretrained models from torchvision
# These models have been trained on ImageNet dataset and can classify images into 1000 categories
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

# Create a dictionary for easy access to models by name
models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load ImageNet class labels mapping from class ID to human-readable label
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    """
    Classify an image using a specified pretrained model.

    Parameters:
    img_path (str): Path to the image to be classified.
    model_name (str): Name of the model to use ('resnet', 'alexnet', or 'vgg').

    Returns:
    str: Human-readable predicted class label.
    """

    # Open the image using PIL
    img_pil = Image.open(img_path)

    # Define preprocessing pipeline: resize, crop, convert to tensor, normalize
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Apply preprocessing to the image
    img_tensor = preprocess(img_pil)
    
    # Add a batch dimension since PyTorch models expect input in batches
    img_tensor.unsqueeze_(0)
    
    # Check PyTorch version to handle changes in Variable API
    pytorch_ver = __version__.split('.')
    
    # For PyTorch 0.4 and higher, Variable is deprecated; just disable gradient computation
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    
    # For older PyTorch versions (<0.4), wrap input tensor in Variable
    else:
        data = Variable(img_tensor, volatile=True)

    # Select the model based on user input
    model = models[model_name]

    # Set model to evaluation mode to disable training-specific operations (e.g., dropout)
    model = model.eval()
    
    # Forward pass: obtain predictions from the model
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    else:
        output = model(data)

    # Identify the index of the class with highest predicted probability
    pred_idx = output.data.numpy().argmax()

    # Return the human-readable class label
    return imagenet_classes_dict[pred_idx]
