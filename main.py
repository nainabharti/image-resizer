import os
from PIL import Image

# Store image path
image_path = "input_images/sample_image1.jpeg"

# Open the image
image = Image.open(image_path)

print("Image opened successfully!")

# Display image properties
print("Width:", image.width)
print("Height:", image.height)
print("Size:", image.size)

# Take new dimensions from user
new_width = int(input("Enter new width: "))
new_height = int(input("Enter new height: "))

# Store dimensions in a tuple
new_dimensions = (new_width, new_height)

# Resize the image
resized_image = image.resize(new_dimensions)

print("\nImage resized successfully!")

# Display resized image properties
print("New Width:", resized_image.width)
print("New Height:", resized_image.height)
print("New Size:", resized_image.size) 

# Create output path
output_path = os.path.join("output_images","sample_image1.jpeg")

# Save resized image
resized_image.save(output_path)

print("\nResized image saved successfully!")
print("Output location:", output_path)