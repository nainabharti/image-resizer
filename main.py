import os
from PIL import Image

# Store input and output folder path
input_folder = "input_images"
output_folder = "output_images"

# Store supported image extensions
supported_extensions = [".jpg", ".jpeg", ".png", ".webp"]

# Get all filename from input folder
files = os.listdir(input_folder)

print("Processing images....\n")

# Process each supported image
for filename in files:

    # Check whether the file has a supported extension
    if filename.lower().endswith(tuple(supported_extensions)):

        # Create input image path
        image_path = os.path.join(input_folder, filename)

        # Open the image
        image = Image.open(image_path)

        print("Image opened:", filename)

        # Display original dimensions
        print("Original Size:", image.size)

        # Take new dimensions from user
        new_width = int(input("Enter new width: "))
        new_height = int(input("Enter new height: "))

        # Store dimensions in a tuple
        new_dimensions = (new_width, new_height)

        # Resize the image
        resized_image = image.resize(new_dimensions)

        # Create output path using original filename
        output_path = os.path.join(output_folder, filename)

        # Save resized image
        resized_image.save(output_path)

        print("Image resized and saved successfully!")
        print("Output location:", output_path)
        print("-" * 40)

print("All supported images processed!")