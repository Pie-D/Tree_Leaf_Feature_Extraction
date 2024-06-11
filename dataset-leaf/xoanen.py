from rembg import remove
from PIL import Image

# Define input and output paths
input_path = 'input.png'
output_path = 'output.png'

# Read the input image
with open(input_path, 'rb') as i:
    input_data = i.read()

# Remove the background
output_data = remove(input_data)

# Save the processed image
with open(output_path, 'wb') as o:
    o.write(output_data)

print("Background removed. Output saved to", output_path)
