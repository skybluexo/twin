from PIL import Image
import os

# Open the image
img = Image.open('frontend/public/avatar.jpg')
print(f'Current dimensions: {img.size}')
print(f'Current size: {os.path.getsize("frontend/public/avatar.jpg") / 1024:.2f} KB')

# Get dimensions
width, height = img.size

# Crop to square from the top (keep top section)
# Use the width as the size, crop from top
if height > width:
    # Portrait: crop from top, keep full width
    crop_size = width
    left = 0
    top = 0
    right = width
    bottom = crop_size
else:
    # Landscape: crop from top, keep full height
    crop_size = height
    left = 0
    top = 0
    right = crop_size
    bottom = height

# Crop to square from top
img_cropped = img.crop((left, top, right, bottom))
print(f'Cropped to square: {img_cropped.size}')

# Resize to 200x200
img_resized = img_cropped.resize((200, 200), Image.Resampling.LANCZOS)
print(f'Resized to: {img_resized.size}')

# Save with compression to keep under 100KB
img_resized.save('frontend/public/avatar.jpg', 'JPEG', quality=85, optimize=True)
final_size = os.path.getsize('frontend/public/avatar.jpg') / 1024
print(f'Final size: {final_size:.2f} KB')

