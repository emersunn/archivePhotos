# Image Copy and Rename Script

This Python script copies image files from a source directory to a destination directory, renaming them sequentially as image1, image2, image3, and so on.

## Requirements

- Python 3.6 or higher

##Prior to use 

- Make sure your photo library is up-to-date. Go to Settings → iCloud → Download originals to this Mac
- In Photos.app, click on Library → all photos to check the download progress

## Usage

1. Update the `source_dir` variable in the script with the path to your "Photos Library.photoslibrary" folder.
2. Update the `dest_dir` variable in the script with the path to your external, followed by the "ApplePhotosExport" folder.
3. Save the script as `copy_images.py`.
4. Open a terminal and navigate to the directory containing the script.
5. Run the script using the following command:

```bash
python copy_rename_images.py
```
