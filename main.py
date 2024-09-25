import os
from PIL import Image, ImageOps

# Directory containing the PNG files
input_folder = './pngs'  # Replace with your folder path
output_folder = './resized_webp'  # Directory to save resized images

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Target size
target_width = 215
target_height = 120

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize the image while maintaining the aspect ratio (height stays 120)
        width, height = img.size
        new_height = target_height
        new_width = int(width * (new_height / height))
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Calculate the padding needed to make the width 215
        padding = (target_width - new_width) // 2

        # Add white padding to the left and right
        img_padded = ImageOps.expand(img_resized, border=(padding, 0, padding, 0), fill='white')

        # Modify the file name to include "_thumbnail" before the extension
        base_name = os.path.splitext(filename)[0]  # Remove the extension
        new_filename = f"{base_name}_thumbnail.webp"  # Add "_thumbnail" and change to .webp

        # Save the resized image as a webp file with the new name
        output_path = os.path.join(output_folder, new_filename)
        img_padded.save(output_path, 'WEBP')

        print(f"Resized and saved: {filename} as {new_filename}")
