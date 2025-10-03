#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

# =============================================================================
# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-09-24
# REVISED DATE: 2025-10-03
#
# PROFESSIONAL OVERVIEW:
# This module was developed to enhance an AI image classification pipeline by
# ensuring correct identification of whether an image is of a dog or not. The
# code demonstrates the ability to integrate external resources (dog names file),
# process data efficiently, and refine classification outputs in a reliable and
# scalable way. These practices showcase practical skills in Python programming,
# data handling, and problem solving that are applicable to both professional
# projects and freelance opportunities.
#
# OBJECTIVES ACHIEVED:
# 1. Load all recognized dog breed names from an external file into a fast
#    lookup structure (dictionary).
# 2. For each classified image, check both the human-provided label and the AI
#    classifier label against the dog names list.
# 3. Determine and record whether the image label is "a dog" or "not a dog".
# 4. Extend the classification results with these determinations to provide a
#    richer, more accurate output for later analysis.
# 5. Handle edge cases such as multiple classifier names and duplicate entries
#    in the dog names file.
#
# By structuring the logic clearly, this script makes AI model results easier to
# validate and interpret—an essential step in ensuring that solutions are both
# technically sound and practically useful.
# =============================================================================


# --- Classifying Labels as Dogs ---
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # Create dictionary of dog names
    dognames_dic = dict()
    with open(dogfile, "r") as f:
        for line in f:
            dog_name = line.strip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print("** Warning: Duplicate dog name found in dognames.txt:", dog_name)
    
    # Process results_dic to add indices 3 & 4
    for key in results_dic:
        # Get pet label
        pet_label = results_dic[key][0]

        # Check if pet label is a dog
        if pet_label in dognames_dic:
            is_pet_dog = 1
        else:
            is_pet_dog = 0
        
        # Check if classifier label (may contain multiple names) is a dog
        classifier_label = results_dic[key][1]
        classifier_names = [name.strip() for name in classifier_label.lower().split(",")]

        is_classifier_dog = 0
        for name in classifier_names:
            if name in dognames_dic:
                is_classifier_dog = 1
                break
        
        # Add new values (index 3 & 4)
        results_dic[key].extend([is_pet_dog, is_classifier_dog])
