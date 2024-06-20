import os
from PIL import Image, ImageEnhance

# Define the path to your folder containing images
folder_path = 'C:/Users/Insight/Downloads/a'

# Create an output folder for enhanced images
output_folder = os.path.join(folder_path, 'enhanced')
os.makedirs(output_folder, exist_ok=True)

# Enhancement parameters
brightness_factor = 1.5  # Adjust as needed
contrast_factor = 1.5    # Adjust as needed
sharpness_factor = 2.0   # Adjust as needed

# Step 1: Rename the files using numbers
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
        new_filename = f'{index + 1:04d}.jpg'  # Renaming to 0001.jpg, 0002.jpg, etc.
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)

# Step 2: Process each image in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
        # Open an image file
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            # Enhance brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_factor)
            
            # Enhance contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_factor)
            
            # Enhance sharpness
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(sharpness_factor)
            
            # Save the enhanced image to the output folder
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

print(f'Enhanced images have been saved to {output_folder}')
