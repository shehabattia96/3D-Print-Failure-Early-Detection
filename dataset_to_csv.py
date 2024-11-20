import os
import cv2
import csv
import re

def process_images_to_csv(
        input_folder:str, 
        output_csv:str, 
        label:str, 
        resize_images_to: tuple[int,int]
        ):
    """
    Reads all image files in a folder, resizes them, flattens and saves them to a CSV file with specified label.
    
    Args:
        input_folder (str): Path to the folder containing image files.
        output_csv (str): Path to the output CSV file.
        label (int): The label value to assign to all rows.
        resize_images_to (tuple): Size to resize input images to before flattening
    """
    # Get list of files in the folder
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    data = []
    for file in files:
        file_path = os.path.join(input_folder, file)
        print("On file ", file)
        
        # Read the image
        image = cv2.imread(file_path)
        if image is None:
            print(f"Warning: Could not read {file}. Skipping.")
            continue
        
        # Resize
        resized_image = cv2.resize(image, resize_images_to)
        
        # Flatten the image to a single row
        flattened_image = resized_image.flatten()
        
        # Extract classname and remove suffix ending in "_{number}"
        # e.g. bed_not_stick_0.png -> bed_not_stick 
        filename_no_extension = os.path.splitext(file)[0]
        match = re.match(r"^(.*)_\d+$", filename_no_extension)
        classname = match.group(1) if match else filename_no_extension
        
        # Prepend label and filename
        row = [label, classname, file] + flattened_image.tolist()
        data.append(row)
    
    print("Saving csv..")
    # Save to CSV
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        header = ['label', 'class', 'filename'] + [f'pixel_{i}' for i in range(len(data[0]) - 3)]

        writer.writerow(header)
        writer.writerows(data)

    print(f"Processing complete. Saved to {output_csv}.")

input_folder = 'datasets/3d-printer-defected-dataset'
labels = ["defected", "not_defected"]
for label in labels:
    process_images_to_csv(
        input_folder=f"{input_folder}/{label}",
        output_csv=f"{label}.csv",
        label=label,
        resize_images_to=(256, 192)
    )
