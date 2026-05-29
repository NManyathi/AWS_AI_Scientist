# 🐶 Case Study: Dog Breed Image Classification using Pretrained CNN Models  

**Project:** AWS AI Scientist – Dog Breed Classifier  
**Models Used:** AlexNet, VGG16, ResNet18  
**Tech Stack:** Python, PyTorch, Torchvision, Bash, Git  

---

## 📌 Problem Statement  

The goal of this project was to build an image classification system capable of identifying dog breeds from images using pretrained Convolutional Neural Network (CNN) models.  

A secondary objective was to evaluate how well different pretrained architectures perform on real-world images and distinguish between:
- Correct dog breed classification  
- Correct identification of dogs vs non-dogs  
- Misclassifications between similar breeds  

---

## 🎯 Objectives  

- Extract true labels from image filenames  
- Classify images using pretrained CNN models (AlexNet, VGG16, ResNet18)  
- Compare predicted labels with actual labels  
- Evaluate model performance across:
  - Dog vs non-dog classification accuracy  
  - Breed-level classification accuracy  
- Test model robustness using different image sets (standard + uploaded custom images)  
- Generate structured performance reports for analysis  

---

## ⚙️ Approach  

### 1. Data Preparation  

Images were stored in a structured dataset where the true label was derived from the filename. A helper function was used to extract and clean labels.

### 2. Model Classification  

Pretrained CNN models from PyTorch were used:
- **AlexNet** → lightweight baseline model  
- **VGG16** → deeper architecture with improved feature extraction  
- **ResNet18** → residual learning model with stronger generalization  

Each image was passed through the selected model to generate predicted labels.

---

### 3. Evaluation Logic  

Each prediction was evaluated at three levels:
- ✔ Is the image correctly identified as a dog or not?  
- ✔ Does the model match the correct breed?  
- ✔ How consistent is the model across different architectures?  

---

### 4. Testing Strategy  

Two datasets were used:
- **Standard dataset:** provided pet images  
- **Uploaded test set:** custom images to test real-world generalization  

This helped evaluate how stable each model is outside the original dataset.

---

## 📊 Key Results (High-Level)  

- High accuracy in **dog vs non-dog classification across all models**  
- VGG16 and ResNet18 showed stronger performance in **breed-level classification**  
- AlexNet performed well but showed more misclassifications on visually similar breeds  
- Models handled standard dataset better than custom uploaded images, showing expected generalization limits  

---

## 🔍 Key Insights  

- Deeper architectures (VGG, ResNet) improve feature recognition for fine-grained classification tasks  
- Misclassifications often occur between visually similar breeds (e.g., terriers, retrievers)  
- Model performance depends heavily on image quality and dataset variability  
- Pretrained CNNs generalize well for dog detection, but breed classification remains challenging  

---

## 🧩 Tools & Skills Demonstrated  

- Deep Learning (CNNs with PyTorch)  
- Image classification pipeline design  
- Model evaluation and comparison  
- Data preprocessing and label extraction  
- Shell scripting for batch testing  
- Git version control and project structuring  

---

## 🚀 Outcome  

This project demonstrates the ability to design, test, and evaluate machine learning pipelines using pretrained deep learning models. It highlights practical experience in computer vision, model comparison, and performance analysis — all essential for real-world AI systems.

---

## Author
**Walter Njabulo Manyathi** 
BSc Applied Mathematics and Statistics
📍 Data Analyst | Statistician | AWS AI Scientist Scholar  
