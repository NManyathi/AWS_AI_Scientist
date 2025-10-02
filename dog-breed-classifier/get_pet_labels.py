#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

# ------------------------------------------------------------------------------
# Professional Note:
# This script demonstrates the ability to design clean, reusable, and 
# production-ready Python functions for real-world machine learning workflows. 
# By converting raw filenames into structured labels, the solution highlights 
# key skills in data preprocessing, automation, and building reliable pipelines. 
# Such approaches are essential in professional environments where clarity, 
# maintainability, and trust in data pipelines are priorities.
# ------------------------------------------------------------------------------

# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-09-22                                  
# REVISED DATE: 2025-10-01

# OBJECTIVE OVERVIEW:
# - Import necessary utilities for file handling.
# - Read filenames from a directory of images.
# - Convert filenames into clean, human-readable pet labels.
# - Ensure labels are standardized: lowercase, alphabetic only, and properly spaced.
# - Store results in a dictionary where:
#     Key   = original filename
#     Value = list containing the processed pet label
# - Handle hidden/system files gracefully.
# - Warn if duplicate filenames are encountered (for robustness).

# ------------------------------------------------------------------------------
# Section: File Handling
# Responsibility: Import required Python modules for listing directory contents.
# ------------------------------------------------------------------------------
from os import listdir

# ------------------------------------------------------------------------------
# Section: Creating Pet Image Labels
# Responsibility: Define a function that extracts and formats pet labels from 
#                 filenames, ensuring labels can be used for classification 
#                 accuracy checks in later project stages.
# ------------------------------------------------------------------------------
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These labels represent the true identity of the pet 
    in the image and will be used to check the classifier's accuracy.

    Example:
        Filename = 'Boston_terrier_02259.jpg'
        Pet label = 'boston terrier'

    Parameters:
        image_dir - Path to the folder containing image files (string).

    Returns:
        results_dic - Dictionary where:
            key   = image filename (string)
            value = list containing one item:
                    index 0 = pet image label (string)
    """

    # Retrieve filenames from directory
    filenames = listdir(image_dir)

    # Initialize empty dictionary to store results
    results_dic = dict()

    # Process each filename to create a pet label
    for filename in filenames:
        # Skip hidden/system files (e.g., .DS_Store)
        if filename.startswith('.'):
            continue
        
        # Convert to lowercase and split by underscore
        lower_filename = filename.lower()
        name_parts = lower_filename.split('_')

        # Keep only alphabetic parts (skip numbers, extensions)
        pet_name_words = [word for word in name_parts if word.isalpha()]

        # Join the words to make the pet label
        pet_label = ' '.join(pet_name_words).strip()

        # Add to dictionary, warn if duplicate key detected
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Key=", filename, 
                  "already exists in results_dic with value =", 
                  results_dic[filename])
    
    return results_dic
