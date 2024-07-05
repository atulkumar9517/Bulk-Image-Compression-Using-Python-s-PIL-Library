import os
from PIL import Image

# Define the directory containing the images
directory = r'C:\Users\Atul\Downloads\Abstract'

# Define the target directory for compressed images
target_directory = os.path.join(directory, 'Compressed')

# Create the target directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Supported image formats
supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Construct the full file path
    file_path = os.path.join(directory, filename)
    
    # Skip directories and non-image files
    if os.path.isdir(file_path) or not filename.lower().endswith(supported_formats):
        continue

    try:
        # Open an image file
        with Image.open(file_path) as img:
            # Get the image format
            img_format = img.format

            # Define the output path
            output_path = os.path.join(target_directory, filename)

            # Save the image with a quality parameter to compress without losing quality
            if img_format == 'JPEG' or img_format == 'JPG':
                img.save(output_path, format=img_format, quality=20, optimize=True)
            else:
                img.save(output_path, format=img_format, optimize=True)
            
            print(f"Compressed: {file_path} -> {output_path}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred with {file_path}: {e}")

print("Image compression complete.")
