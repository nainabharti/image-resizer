from PIL import Image

# Store image path
image_path = "input_images/sample_image1.jpeg"

# Open the image
image = Image.open(image_path)

print("Image opened successfully!")

# Display image properties
print("Width:", image.width)
print("Height:",image.height)
print("Size:", image.size)