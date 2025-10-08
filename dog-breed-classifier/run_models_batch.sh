#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch.sh
#                                                                             
# PROGRAMMER: Walter Njabulo Manyathi
# DATE CREATED: 2025-10-06                                  
# REVISED DATE: 
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh    -- will run program from commandline within Project Workspace
#  
# For my setup, I found Git Bash to be the most reliable way to run this script on Windows.
# If you’re on Windows, use WSL or Git Bash. On Linux/Mac, open the VS Code terminal and run:
# chmod +x run_models_batch.sh 
# Then execute the script with: ./run_models_batch.sh
# This approach solves common permission or path issues often faced when running scripts directly from VS Code.

#
# Run Resnet on pet_images and save results
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > results_resnet.txt

# Run AlexNet on pet_images and save results 
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > results_alexnet.txt

# Run Vgg on pet_images and save results
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > results_vgg.txt

echo "All models run on pet_images completed!"