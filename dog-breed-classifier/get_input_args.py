#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: get_input_args.py
#
# ------------------------------------------------------------
# Project: AI Programming with Python Nanodegree Revision
# Module: Command Line Argument Handling
# Author: Walter Njabulo Manyathi
# Created: 2025-09-22
# REVISED DATE: 2025-09-30
# ------------------------------------------------------------
# PROFESSIONAL SUMMARY:
# This script demonstrates robust use of Python's argparse library
# to handle command line arguments in a flexible and professional way.
# It is designed for real-world AI/ML projects, where modularity,
# scalability, and usability are essential. By making the program
# configurable from the terminal, we enable seamless testing, automation,
# and integration into larger pipelines—qualities employers and clients
# look for in production-ready code.
#
# OBJECTIVES (explained simply):
# 1. Allow the user to specify an image folder without editing code.
# 2. Let the user choose a CNN model architecture (e.g., vgg, resnet, alexnet).
# 3. Provide a way to supply a text file of valid dog names.
# 4. Ensure defaults exist so the program still runs if arguments are omitted.
# 5. Return all inputs in a structured format that can be used across the project.
#
# SECTION: Command Line Argument Handling
# Purpose: Retrieve and parse external inputs passed to the program
#          via terminal commands using argparse.
# ------------------------------------------------------------

import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 

    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images/'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'

    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(
        description="Retrieve command line arguments for the Dog Breed Classifier project"
    )
    
    # Define 3 command line arguments with portable default paths
    parser.add_argument(
        '--dir',
        type=str,
        default='pet_images/',
        help='Path to the folder of pet images (default: pet_images/)',
    )
    parser.add_argument(
        '--arch',
        type=str,
        default='vgg',
        choices=['vgg', 'resnet', 'alexnet'],
        help='CNN model architecture to use: vgg, resnet, alexnet (default: vgg)',
    )
    parser.add_argument(
        '--dogfile',
        type=str,
        default='dognames.txt',
        help='Text file containing names of dog breeds (default: dognames.txt)',
    )
    
    # Parse and return arguments
    return parser.parse_args()
