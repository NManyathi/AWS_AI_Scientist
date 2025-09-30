#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check_images.py
#
# ---------------------------------------------------------------------------
# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-09-22
# REVISED DATE: 2025-09-29
#
# PROJECT OVERVIEW:
# This script is designed to classify pet images using pre-trained CNN 
# (Convolutional Neural Network) architectures. It extracts labels directly 
# from image filenames, compares them against model predictions, and produces 
# detailed performance statistics. The program demonstrates:
#   1. How to integrate deep learning models into end-to-end workflows.
#   2. The importance of preprocessing, validation, and statistical analysis.
#   3. Practical application of command-line tools in a professional environment.
#
# VALUE FOR EMPLOYERS / CLIENTS:
# - Highlights ability to build clean, modular, and maintainable Python programs.
# - Demonstrates practical use of AI/ML models alongside validation and evaluation.
# - Reflects experience in creating production-ready scripts with clear runtime 
#   tracking and performance reporting.
# ---------------------------------------------------------------------------

from time import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # ------------------ Section: Runtime Measurement (Start) ------------------
    start_time = time()

    # ------------------ Section: Command-Line Argument Parsing ------------------
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # ------------------ Section: Extracting Pet Image Labels ------------------
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # ------------------ Section: Classifying Images ------------------
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    # ------------------ Section: Adjusting Results for Dog Classification ------------------
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # ------------------ Section: Calculating Statistics ------------------
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # ------------------ Section: Printing Final Results ------------------
    print_results(results, results_stats, in_arg.arch, True, True)

    # ------------------ Section: Runtime Measurement (End) ------------------
    end_time = time()
    tot_time = end_time - start_time
    hours = int(tot_time // 3600)
    minutes = int((tot_time % 3600) // 60)
    seconds = int((tot_time % 3600) % 60)
    print("\n** Total Elapsed Runtime: {}:{}:{}".format(hours, minutes, seconds))


if __name__ == "__main__":
    main()
