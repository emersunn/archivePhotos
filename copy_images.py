import os
import shutil
from pathlib import Path

# Set the source and destination directories
source_dir = "/Users/username/Pictures/Photos Library.photoslibrary/originals"
dest_dir = "/Volumes/drivename/OriginalPhotos"

# Get all files in the source directory
all_files = [f for f in Path(source_dir).rglob("*") if f.is_file()]

# Filter only image files
image_extensions = {'.jpg', '.cr2', '.arw', '.jpeg', '.png', '.heic', '.bmp', '.tiff'}
image_files = [f for f in all_files if f.suffix.lower() in image_extensions]
    
# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Copy and rename image files to the destination directory
counter = 1
for img in image_files:
    # Construct the new filename
    new_name = f"image{counter}{img.suffix}"

    # Copy and rename the image
    shutil.copy2(img, os.path.join(dest_dir, new_name))

    # Increment the counter
    counter += 1

print("Original images copied and renamed successfully.")
