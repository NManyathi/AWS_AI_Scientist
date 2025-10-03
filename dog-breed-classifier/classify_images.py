#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# classify_images.py
#
# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-09-22
# REVISED DATE: 2025-10-02
#
# PROFESSIONAL PURPOSE:
# This module demonstrates the ability to apply deep learning techniques to
# real-world image classification tasks. It showcases competence in Python,
# CNN model integration, and data handling. Employers and freelance clients
# can quickly see the practical skills in automating image recognition,
# comparing results to expected labels, and preparing structured output.
#
# OBJECTIVES:
# 1. Accept a folder of images and a dictionary containing pet image labels.
# 2. Use a Convolutional Neural Network (CNN) model to classify each image.
# 3. Format the classifier's labels for comparison with pet image labels.
# 4. Compare classifier labels to pet labels and mark matches.
# 5. Store the classifier results and match information in the existing
#    results dictionary for further evaluation or reporting.

import os
from classifier import classifier

# Classifying Images
# This section defines the function that creates classifier labels, compares
# them to pet labels, and updates the results dictionary accordingly.
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the CNN classifier, compares them to pet
    labels, and adds the classifier label and match indicator to the results dictionary.
    
    Parameters: 
      images_dir - Full path to the folder containing the images (string)
      results_dic - Dictionary where key = filename and value = list containing:
                    index 0 = pet image label (string)
                    index 1 = classifier label (string) [added by this function]
                    index 2 = match indicator 1/0 (int) [added by this function]
      model - CNN architecture to use for classification ('resnet', 'alexnet', 'vgg')
    
    Returns:
      None - results_dic is updated in-place
    """
    
    # Iterate through each image in the results dictionary
    for filename in results_dic:
        # Build the full path to the image dynamically
        image_path = os.path.join(images_dir, filename)

        # Obtain classifier label using the CNN model
        classifier_label = classifier(image_path, model)
        
        # Normalize the classifier label for comparison
        classifier_label = classifier_label.lower().strip()
        
        # Retrieve the pet image label from the results dictionary
        pet_label = results_dic[filename][0]
        
        # Determine if the pet label matches the classifier label
        match = 1 if pet_label in classifier_label else 0
        
        # Extend the results dictionary with classifier label and match
        results_dic[filename].extend([classifier_label, match])
