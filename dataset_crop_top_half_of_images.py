"""
Cropping the top half of the images that don't have much information for our training
"""

import os
from PIL import Image

def crop_top_half_recursive(input_dir, output_dir):
    """
    Crop the top half of images in a folder recursively and save them to a new folder, 
    preserving the folder structure.

    Args:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
    """
    # Walk through the input directory
    for root, _, files in os.walk(input_dir):
        # Determine the corresponding output folder
        relative_path = os.path.relpath(root, input_dir)
        output_folder = os.path.join(output_dir, relative_path)
        
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        for file in files:
            input_file = os.path.join(root, file)
            output_file = os.path.join(output_folder, file)
            
            # Process only image files
            try:
                with Image.open(input_file) as img:
                    width, height = img.size
                    cropped_img = img.crop((0, height // 2, width, height))
                    cropped_img.save(output_file)
                    print(f"Cropped: {input_file} -> {output_file}")
            except Exception as e:
                print(f"Skipping {input_file}: {e}")

if __name__ == "__main__":
    # Replace with your input and output directories
    input_directory = "datasets/v1_balanced_images/"
    output_directory = "datasets/v2_balanced_images_cropped_top_half/"

    crop_top_half_recursive(input_directory, output_directory)
