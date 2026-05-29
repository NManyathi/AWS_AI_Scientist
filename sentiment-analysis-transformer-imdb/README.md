## 👨🏽‍💻 Author
**Walter Njabulo Manyathi**  
📍 Data Analyst | Statistician | AWS AI Scholar  
🔗 [GitHub](https://github.com/NManyathi) • [LinkedIn](https://www.linkedin.com/in/walter-njabulo-manyathi-0b4981172/)

---

# 🧠 SentimentScope – IMDB Sentiment Analysis using Transformers

This project implements a **custom transformer-based deep learning model** for sentiment analysis on the IMDB movie review dataset. The model classifies reviews as either **positive** or **negative** using transformer attention mechanisms and NLP preprocessing techniques.

The project was completed as part of the **Udacity AWS AI Scientist Scholarship** learning journey.

---

## 📌 Project Overview

The objective of this project was to:

1. Load and preprocess the IMDB movie review dataset
2. Tokenize raw text using a pretrained BERT tokenizer
3. Build a custom transformer architecture from scratch
4. Train the model for binary sentiment classification
5. Evaluate model performance on validation and test datasets
6. Achieve test accuracy above 75%

---

## 📂 Project Structure

```bash
.
├── README.md                                   # Project documentation
├── sentimentscope-imdb-transformer.ipynb       # Main notebook containing full implementation
├── case_study.md                               # Detailed project case study
├── aclImdb_v1.tar.gz                           # IMDB dataset archive
└── sentiment-analysis-transformer-badge.png    # Udacity project completion badge
```

---

## ⚙️ How It Works

### 1. Dataset Preparation

This project uses the IMDB Movie Reviews Dataset, which contains 50,000 labeled movie reviews for binary sentiment classification (positive or negative).

The dataset is automatically:

Loaded from the compressed archive
Extracted into the project directory
Split into:
Training dataset
Validation dataset
Test dataset

This preparation step ensures the data is organized correctly before transformer model training begins.

📥 Dataset Download

The dataset is not included in this repository because the archive size exceeds GitHub's recommended file size limits.

Download the IMDB dataset from the official Stanford AI Lab source:

https://ai.stanford.edu/~amaas/data/sentiment/

After downloading, place the following file inside the project root directory:

aclImdb_v1.tar.gz

The notebook will automatically extract and prepare the dataset during execution.

---

### 2. Text Processing

The project uses the `bert-base-uncased` tokenizer from Hugging Face.

Processing steps include:

* Tokenization
* Padding
* Truncation
* Tensor conversion for PyTorch

Maximum sequence length:

```python
MAX_LENGTH = 128
```

---

### 3. Transformer Architecture

The custom transformer model includes:

* Token embeddings
* Positional embeddings
* Multi-head self-attention
* Feedforward neural networks
* Layer normalization
* Mean pooling for sequence representation
* Classification head for binary sentiment prediction

---

### 4. Model Training

Training configuration:

| Parameter     | Value            |
| ------------- | ---------------- |
| Optimizer     | AdamW            |
| Loss Function | CrossEntropyLoss |
| Batch Size    | 32               |
| Epochs        | 3                |
| Device        | GPU (CUDA)       |

Validation accuracy is calculated after every epoch to monitor learning progress.

---

## 🧩 Skills Demonstrated

- Natural Language Processing (NLP)
- Transformer architecture implementation
- Text preprocessing and tokenization
- PyTorch deep learning workflows
- Binary sentiment classification
- Model evaluation and validation tracking
- GPU-based model training
- Attention mechanism implementation

---

## 📊 Final Results

| Metric              | Result     |
| ------------------- | ---------- |
| Validation Accuracy | **78.56%** |
| Test Accuracy       | **76.40%** |

The model successfully exceeded the target accuracy threshold of 75%.

---

## ✅ Key Findings

* Transformer architectures are highly effective for NLP classification tasks
* Attention mechanisms help capture contextual meaning in text
* Proper tokenization and padding significantly improve model performance
* Validation tracking helps monitor learning stability and model generalization
* Training accuracy improved steadily across epochs

---

## 🛠️ Technologies Used

* **Python 3**
* **PyTorch**
* **Hugging Face Transformers**
* **Pandas**
* **Matplotlib**
* **GPU Training (CUDA)**

---

## 🚀 How to Reproduce

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd sentimentscope-transformer
```

---

### 2. Install Dependencies

```bash
pip install torch transformers pandas matplotlib scikit-learn
```

---

### 3. Open the Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```bash
sentimentscope-imdb-transformer.ipynb
```

---

### 4. Run the Notebook

Execute the notebook cells sequentially to:

* Extract the dataset
* Preprocess text
* Train the transformer model
* Evaluate accuracy

---

## 📌 Deliverables

* Fully functional transformer-based sentiment classifier
* End-to-end NLP pipeline implementation
* Performance evaluation on unseen IMDB reviews
* Case study documentation
* Project completion badge

---

## 📘 Lessons Learned

* Understanding transformer attention mechanisms
* Building custom transformer architectures in PyTorch
* Importance of tokenization and sequence preprocessing
* Training deep learning models on GPU environments
* Evaluating model generalization using validation and test datasets

---

## ⭐ Final Note

Built as part of the **Udacity AWS AI Scientist Scholarship** program, focused on practical implementation of transformer-based Natural Language Processing (NLP) systems.

---

## 🔮 Future Improvements  

Potential improvements for future versions of this project include:

- Training the transformer model for more epochs to improve accuracy  
- Experimenting with larger embedding dimensions and deeper transformer layers  
- Adding learning rate scheduling for more stable training  
- Comparing custom transformer performance against pretrained BERT classifiers  
- Visualizing training and validation loss using graphs  
- Deploying the sentiment classifier as a simple web application  

---