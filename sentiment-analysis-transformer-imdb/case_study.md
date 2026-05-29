# 🧠 Case Study: SentimentScope – Sentiment Analysis using Transformers

**Project:** SentimentScope (IMDB Sentiment Classifier)
**Model Architecture:** Custom Transformer (BERT-based tokenizer + attention blocks)
**Tech Stack:** Python, PyTorch, Hugging Face Transformers, Pandas, Matplotlib

---

## 📌 Problem Statement

The goal of this project was to build a sentiment analysis system capable of classifying IMDB movie reviews as either positive or negative using a transformer-based deep learning model.

A key objective was to understand how transformer architectures perform on real-world text classification tasks and evaluate their ability to generalize to unseen movie reviews.

---

## 🎯 Objectives

* Load and preprocess the IMDB sentiment dataset
* Convert raw text into tokenized inputs using a pretrained tokenizer
* Build a transformer-based neural network for classification
* Train and evaluate the model on labeled movie reviews
* Measure performance using validation and test accuracy
* Achieve a target accuracy above 75%

---

## ⚙️ Approach

### 1. Data Preparation

The IMDB dataset containing 50,000 labeled reviews was loaded and structured into training, validation, and test sets. Exploratory analysis was performed to understand label distribution and review length patterns.

---

### 2. Text Processing

* Used `bert-base-uncased` tokenizer from Hugging Face
* Applied tokenization, truncation, and padding (`max_length = 128`)
* Converted text into PyTorch tensors for model input

---

### 3. Model Development

A custom transformer architecture was implemented including:

* Token and positional embeddings
* Multi-head self-attention layers
* Feedforward neural network blocks
* Layer normalization

For classification:

* Mean pooling was applied over token embeddings
* A linear classification head was added for binary output

---

### 4. Training Strategy

* **Loss Function:** CrossEntropyLoss
* **Optimizer:** AdamW
* **Batch Size:** 32
* **Training Duration:** 3 epochs
* Validation used after each epoch for monitoring

---

## 📊 Key Results

| Metric              | Result     |
| ------------------- | ---------- |
| Validation Accuracy | **78.56%** |
| Test Accuracy       | **76.40%** |

The model successfully exceeded the target performance threshold of 75%, demonstrating strong generalization on unseen data.

---

## 🔍 Key Insights

* Transformer models effectively capture contextual meaning in text
* Proper tokenization and padding are critical for performance
* Validation tracking helps detect learning progress and stability
* Performance improves significantly after initial training epochs
* Mean pooling provides a simple yet effective classification strategy

---

## 🧩 Challenges & Solutions

### Challenge 1: Understanding Transformer Architecture

Initially, the transformer architecture was difficult to understand due to the complexity of attention mechanisms and layered computations.

**Solution:**
The model was broken into modular components such as attention heads, feedforward layers, and transformer blocks, making implementation easier to manage and debug.

---

### Challenge 2: Text Preprocessing Complexity

Handling variable-length text sequences created challenges during batching and model input preparation.

**Solution:**
Padding and truncation strategies were implemented using the Hugging Face tokenizer to ensure all sequences maintained a consistent input length.

---

### Challenge 3: Low Initial Performance

The model initially achieved close to random prediction accuracy (~50%) because weights were randomly initialized.

**Solution:**
Performance improved gradually through multiple training epochs, optimization tuning, and validation monitoring.

---

## 🛠 Tools & Skills Demonstrated

* Deep Learning (Transformer Models)
* Natural Language Processing (NLP)
* PyTorch Model Development
* Hugging Face Tokenization
* Model Evaluation & Performance Tracking
* Data Preprocessing and Analysis
* GPU-based Training Workflows

---

## 🚀 Outcome

This project demonstrates the successful development of a transformer-based sentiment analysis system capable of classifying movie reviews with strong accuracy.

It highlights practical experience in:

* Building end-to-end NLP pipelines
* Implementing transformer architectures from scratch
* Training and evaluating deep learning models
* Working with tokenization and attention mechanisms
* Evaluating model generalization on unseen datasets

The final system achieved reliable performance and provides a strong foundation for real-world sentiment analysis applications.

---

## ⭐ Final Note

Built as part of the Udacity AWS AI Scientist Scholarship learning journey, with a focus on transformer-based Natural Language Processing (NLP) applications and practical deep learning implementation.

---

## Author
**Walter Njabulo Manyathi** 
BSc Applied Mathematics and Statistics
📍 Data Analyst | Statistician | AWS AI Scientist Scholar  