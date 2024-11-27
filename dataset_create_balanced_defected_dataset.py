"""
We're mixing data from different datasets, and categorizing defected and not-defected.
We would like the number of samples to remain similar in each category, so that the samples remain balanced.
This script will randomly sample images from defected folders and create a new defected folder
"""

import os
import random
import shutil

def sample_and_copy(src_folders, dst_folder, sample_size):
    """
    Randomly samples files from each source folder and copies them to the destination folder.

    Args:
        src_folders (list of str): List of source folder paths.
        dst_folder (str): Destination folder path.
        sample_size (int): Number of files to sample from each folder.
    """
    # Create the destination folder if it doesn't exist
    os.makedirs(dst_folder, exist_ok=True)

    for folder in src_folders:
        if not os.path.exists(folder):
            print(f"Source folder not found: {folder}")
            continue

        # Get a list of files in the folder
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

        # If there are fewer files than the sample size, warn the user
        if len(files) < sample_size:
            print(f"Warning: Only {len(files)} files in folder '{folder}', less than the requested {sample_size}.")
            sampled_files = files  # Use all available files
        else:
            sampled_files = random.sample(files, sample_size)  # Randomly sample files

        # Copy sampled files to the destination folder
        for file in sampled_files:
            src_path = os.path.join(folder, file)
            dst_path = os.path.join(dst_folder, file)
            shutil.copy(src_path, dst_path)
            print(f"Copied: {src_path} -> {dst_path}")

if __name__ == "__main__":
    base_source_path = 'datasets/v0_just_the_datasets_we_are_interested_in/'

    source_folders = ["defected", "Off_platform", "Warping"]
    source_folders = [base_source_path + folder for folder in source_folders]

    # Define destination folder
    destination_folder = "datasets/v1_balanced_images/defected"
    
    # Number of files to sample from each folder, chosed based on the number of images in the not-defected folder:
    files_to_sample = int( 792/3)

    sample_and_copy(source_folders, destination_folder, files_to_sample)
