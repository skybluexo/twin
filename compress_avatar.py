from PIL import Image
import os

# Open the original image
img = Image.open('frontend/public/avatar.jpg')
original_size = os.path.getsize('frontend/public/avatar.jpg') / 1024
print(f'Original size: {original_size:.2f} KB')
print(f'Original dimensions: {img.size}')

# Resize to a reasonable size (max 800px on longest side)
max_size = 800
ratio = min(max_size / img.width, max_size / img.height)
new_size = (int(img.width * ratio), int(img.height * ratio))
img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
print(f'Resized dimensions: {new_size}')

# Try different quality levels to get under 100KB
quality = 75
final_size = 0

while quality >= 50:
    img_resized.save('frontend/public/avatar_compressed.jpg', 'JPEG', quality=quality, optimize=True)
    size_kb = os.path.getsize('frontend/public/avatar_compressed.jpg') / 1024
    print(f'Quality {quality}: {size_kb:.2f} KB')
    
    if size_kb < 100:
        final_size = size_kb
        break
    
    quality -= 5

if final_size == 0:
    # If still too large, resize smaller
    max_size = 600
    ratio = min(max_size / img.width, max_size / img.height)
    new_size = (int(img.width * ratio), int(img.height * ratio))
    img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
    img_resized.save('frontend/public/avatar_compressed.jpg', 'JPEG', quality=70, optimize=True)
    final_size = os.path.getsize('frontend/public/avatar_compressed.jpg') / 1024
    print(f'Further resized to {new_size}, final size: {final_size:.2f} KB')

print(f'\nCompression complete! Final size: {final_size:.2f} KB')

