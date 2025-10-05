#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-09-24
# REVISED DATE: 2025-10-04
#
# PROFESSIONAL COMMENT:
# This script was designed as part of an AI-powered image classification project.
# It demonstrates the ability to design, structure, and implement functions that
# process results, generate statistics, and highlight misclassifications.
# The work reflects best practices in software development, data analysis,
# and clear reporting — key skills for professional environments and freelance
# opportunities.c

# OBJECTIVE:
# The purpose of this file is to define a single function `print_results`.
# The function prints:
#   1. A clear summary of classification results.
#   2. Key statistics (counts and percentages).
#   3. Misclassifications, when requested.
# The design ensures the results are both technically useful for debugging
# and accessible for reporting to non-technical stakeholders.
#
# Printing Results

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    FUNCTION OBJECTIVE:
    Print summary results on the image classification task, including
    optional reporting of misclassified dogs and misclassified breeds.

    PARAMETERS:
      results_dic (dict) - Key = image filename, Value = List:
           [0] Pet Image Label (string)
           [1] Classifier Label (string)
           [2] 1/0 -> Labels match? (1 = match, 0 = no match)
           [3] 1/0 -> Pet Image is-a-dog? (1 = yes, 0 = no)
           [4] 1/0 -> Classifier says is-a-dog? (1 = yes, 0 = no)

      results_stats_dic (dict) - Key = statistic name, Value = value
           Example keys: 'n_images', 'n_dogs_img', 'pct_correct_dogs'

      model (str) - CNN architecture used (e.g., 'resnet', 'alexnet', 'vgg')

      print_incorrect_dogs (bool, default=False) -
           If True, prints images incorrectly classified as dogs/not-dogs.

      print_incorrect_breed (bool, default=False) -
           If True, prints images incorrectly classified by breed.

    RETURNS:
      None - This function prints outputs directly.
    """    

    # --- MODEL USED ---
    print("\n\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")

    # --- OVERALL COUNTS ---
    print("{:20}: {:3d}".format('Number of Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('Number of Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('Number of Not-a Dog Images', results_stats_dic['n_notdogs_img']))

    # --- PERCENTAGE STATISTICS ---
    print("\n*** Percentage Statistics ***")
    for key in results_stats_dic:
        if key.startswith('pct'):
            print("{:20}: {:.2f}".format(key, results_stats_dic[key]))
    
    # --- MISCLASSIFIED DOGS ---
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] ) ):
        print("\n*** Misclassified Dogs ***")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:  # disagreement between dog/not-dog
                print("Pet Label: {:>20}  Classifier Label: {:>20}".format(results_dic[key][0], results_dic[key][1]))

    # --- MISCLASSIFIED BREEDS ---
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\n*** Misclassified Breeds ***")
        for key in results_dic:
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):  # both are dogs but labels mismatch
                print("Pet Label: {:>20}  Classifier Label: {:>20}".format(results_dic[key][0], results_dic[key][1]))
