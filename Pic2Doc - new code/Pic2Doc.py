import os
from PIL import Image, ImageEnhance
from docx import Document
from docx.shared import Inches
from docx2pdf import convert

# Define the path to your folder containing images
folder_path = 'C:/Users/Insight/Downloads/a'

# Create an output folder for enhanced images
output_folder = os.path.join(folder_path, 'enhanced')
os.makedirs(output_folder, exist_ok=True)

# Enhancement parameters
brightness_factor = 1.5  # Adjust as needed
contrast_factor = 1.5    # Adjust as needed
sharpness_factor = 2.0   # Adjust as needed

# Create a new Word document
doc = Document()

# Set page layout to A4 and margins to narrow
sections = doc.sections
for section in sections:
    section.page_height = Inches(11.69)
    section.page_width = Inches(8.27)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

# Step 1: Rename the files using numbers, keeping their original extensions
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
        file_extension = os.path.splitext(filename)[1]  # Extract the file extension
        new_filename = f'{index + 1:04d}{file_extension}'  # Use the original extension
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)

# Step 2: Process each image in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
        # Open an image file
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            # Convert image to RGB mode if not already
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
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

            # Add image to Word document
            doc.add_picture(output_path, width=Inches(7.5))  # Adjust width to fit A4 page
            doc.add_page_break()

# Save the Word document
word_output_path = os.path.join(folder_path, 'enhanced_images.docx')
doc.save(word_output_path)

# Convert the Word document to PDF
pdf_output_path = os.path.join(folder_path, 'enhanced_images.pdf')
convert(word_output_path, pdf_output_path)

# Open the PDF file
os.startfile(pdf_output_path)
