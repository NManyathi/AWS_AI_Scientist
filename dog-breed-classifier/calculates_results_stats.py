#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py

# ------------------------------------------------------------
# PROFESSIONAL COMMENT:
# This script demonstrates the ability to design and implement
# a structured evaluation function for an AI image classifier.
# It highlights problem-solving, clean coding practices, and
# the ability to translate project requirements into working
# solutions. The function inside this file calculates key
# performance metrics (counts and percentages) that determine
# the effectiveness of machine learning models. 
# This kind of work is applicable to real-world projects
# in data science, AI, and software development.
# ------------------------------------------------------------

# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-09-24                                 
# REVISED DATE: 2025-10-04

# OBJECTIVES:
# 1. Accept the classifier results in dictionary form.
# 2. Count how many images are dogs, non-dogs, correct matches, and breed matches.
# 3. Compute percentages for matches, correct dogs, correct non-dogs, and correct breeds.
# 4. Return all statistics in a single dictionary for easy reporting and comparison.
# 5. Provide a foundation for determining which AI model performs best.

# Calculating Results
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.
    """        
    # Initialize the results statistics dictionary
    results_stats_dic = dict()
    
    # Initialize counters
    n_images = len(results_dic)  # Total number of images
    n_dogs_img = 0               # Number of dog images
    n_notdogs_img = 0            # Number of NON-dog images
    n_match = 0                  # Number of label matches (regardless of dog)
    n_correct_dogs = 0           # Number of correctly classified dog images
    n_correct_notdogs = 0        # Number of correctly classified NON-dog images
    n_correct_breed = 0          # Number of correctly classified dog breeds

    # Iterate through results_dic to compute counts
    for key in results_dic:
        pet_label_is_dog = results_dic[key][3]
        classifier_label_is_dog = results_dic[key][4]
        labels_match = results_dic[key][2]

        if labels_match == 1:
            n_match += 1
        
        if pet_label_is_dog == 1:
            n_dogs_img += 1
            if classifier_label_is_dog == 1:
                n_correct_dogs += 1
            if labels_match == 1:
                n_correct_breed += 1
        else:  
            n_notdogs_img += 1
            if classifier_label_is_dog == 0:
                n_correct_notdogs += 1
        
    # Calculate percentages
    pct_match = (n_match / n_images) * 100.0 if n_images > 0 else 0.0
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100.0 if n_notdogs_img > 0 else 0.0
    
    # Populate the results_stats_dic dictionary 
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['pct_match'] = pct_match
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
    results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs

    return results_stats_dic
