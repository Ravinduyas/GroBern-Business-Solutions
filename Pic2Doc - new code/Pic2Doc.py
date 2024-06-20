import os
from PIL import Image, ImageEnhance
from docx import Document
from docx.shared import Inches
from docx2pdf import convert

# Define the path to your folder containing images
input_folder = r'C:\Users\Insight\Downloads\New folder (8)'

# Create an output folder for enhanced images
output_folder = os.path.join(input_folder, 'enhanced')
os.makedirs(output_folder, exist_ok=True)

# Enhancement parameters
brightness_factor = 1.5  # Adjust as needed
contrast_factor = 2.5    # Adjust as needed
sharpness_factor = 5.0   # Adjust as needed

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

# Function to rename files in the input folder
def rename_files(folder):
    try:
        # Ensure the folder exists
        if not os.path.isdir(folder):
            print(f"The folder {folder} does not exist.")
            return
        
        # Enumerate through files and rename them
        for i, filename in enumerate(os.listdir(folder)):
            if filename.lower().endswith(".jpeg"):  # Ensure the file extension is case-insensitive
                new_name = f"image_{i + 1}.jpeg"  # Create a new naming pattern
                old_path = os.path.join(folder, filename)
                new_path = os.path.join(folder, new_name)
                
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Rename the files in the input folder
rename_files(input_folder)

# Process each image in the folder
for filename in sorted(os.listdir(input_folder)):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
        # Open an image file
        img_path = os.path.join(input_folder, filename)
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

# Remove the last page break
if doc.paragraphs[-1].text == '':
    doc.paragraphs[-1]._element.getparent().remove(doc.paragraphs[-1]._element)

# Save the Word document
word_output_path = os.path.join(input_folder, 'enhanced_images.docx')
doc.save(word_output_path)

# Convert the Word document to PDF
pdf_output_path = os.path.join(input_folder, 'enhanced_images.pdf')
convert(word_output_path, pdf_output_path)

# Open the PDF file
os.startfile(pdf_output_path)
