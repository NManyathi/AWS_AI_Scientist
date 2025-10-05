# Dog Breed Classifier  

This project uses **a pre-trained deep learning model** to classify images as **dogs vs. not dogs**, and if the image is a dog, it further identifies the **specific dog breed**. It is part of Udacity’s *AI Programming with Python Nanodegree*.

---

## 📌 Project Overview  

The objective is to:
1. **Load and preprocess image data.**  
2. **Use transfer learning** with a pre-trained CNN (Convolutional Neural Network).  
3. **Classify images** into two categories: *dogs* and *not-dogs*.  
4. **For dog images**, predict the **correct breed**.  
5. **Compare the performance** of three different CNN architectures:
   - VGG  
   - ResNet  
   - AlexNet  

---

## 📂 Project Structure  

```
.
├── README.md                # Project documentation
├── run_models_batch.sh      # Script to run all models in one go
├── check_images.py          # Main program for classification
├── classifier.py            # Helper functions for using CNN models
├── classify_images.py       # Classifies images using pretrained CNNs
├── get_pet_labels.py        # Extracts pet labels from image filenames
├── get_input_args.py        # Parses command-line arguments
├── dognames.txt             # List of valid dog names
├── results.txt              # Final results and performance stats
├── adjust_results4_isadog.py # Adjust results dictionary with dog labels
├── calculate_results_stats.py # Compute statistics (accuracy, etc.)
├── print_results.py          # Nicely formatted results output
├── print_functions_for_lab_checks.py
├── data/                    # Folder containing image dataset(Dog-breed-classifier folder)
│   ├── pet_images/           # Training dataset (40+ required images)
│   └── uploaded-test-images_set/ # (Optional) Your own test images
├── certification badge 5    # Certification badge earned for course/project completion
└── saved_results/           # (Optional) Store results from different runs
```

---

## ⚙️ How It Works  

1. **Dataset Preparation**  
   - Place all training images inside the `data/pet_images/` folder (at least 40).  
   - The file names are used as the “ground truth” labels. Example:  
     - `Golden_retriever_1.jpg` → *Golden Retriever*.  

2. **Choose a Model Architecture**  
   The program supports:  
   - `vgg`  
   - `resnet`  
   - `alexnet`  

3. **Run the Program**  
   Run the classifier with a specific architecture:  

   ```bash
   python check_images.py --dir data/pet_images/ --arch vgg --dogfile dognames.txt
   ```

   Or run all models using the batch script:  

   ```bash
   ./run_models_batch.sh
   ```

4. **View Results**  
   Results include:  
   - Total images processed  
   - % correct dogs  
   - % correct breeds  
   - % correct “not-dog” classification  
   - Overall accuracy  

---

## 📊 Example Results  

### VGG  
```
*** Percentage Statistics ***
pct_match           : 87.50
pct_correct_dogs    : 100.00
pct_correct_breed   : 93.33
pct_correct_notdogs : 100.00
```

### ResNet  
```
*** Percentage Statistics ***
pct_match           : 82.00
pct_correct_dogs    : 90.00
pct_correct_breed   : 88.00
pct_correct_notdogs : 95.00
```

### AlexNet  
```
*** Percentage Statistics ***
pct_match           : 75.50
pct_correct_dogs    : 85.00
pct_correct_breed   : 78.00
pct_correct_notdogs : 90.00
```

---

## ✅ Key Findings  

- All three models can distinguish dogs from not-dogs reliably.  
- **VGG** showed the **highest accuracy in breed classification**.  
- **ResNet** also performed strongly but slightly lower.  
- **AlexNet** had the lowest performance, which is expected given it’s an older architecture.  

---

## 🛠️ Technologies Used  

- **Python 3.8+**  
- **PyTorch** (pre-trained models)  
- **NumPy & PIL** for data handling  
- **Shell scripting** for automation  

---

## 🚀 How to Reproduce  

1. Clone this repository:  
   ```bash
   git clone <your-repo-link>
   cd dog-breed-classifier
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Place at least 40 images in `data/pet_images/`.  

4. Run:  
   ```bash
   python check_images.py --dir data/pet_images/ --arch vgg --dogfile dognames.txt
   ```

---

## 📌 Deliverables  

- **Results printed to console** (or redirected to a file).  
- **results.txt** file for submission.  
- Well-structured code with modular functions.  

---

## ✨ Lessons Learned  

- Importance of **transfer learning** in saving training time.  
- Strengths and weaknesses of different CNN architectures.  
- How to preprocess data and evaluate model performance.  
