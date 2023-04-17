# Image Copy and Rename Script

This Python script copies image files from a source directory to a destination directory, renaming them sequentially as image1, image2, image3, and so on.

## Requirements

- Python 3.6 or higher
- Local drive large enough to hold your Photo library
- External drive large enough to handle the export

## Prior to use 

- Make sure your photo library is up-to-date. In Photos.app go to Settings → iCloud → Download originals to this Mac
- While still in Photos.app, click on Library → all photos to check the download progress
- Once all photos are downloaded execute the script

## Usage

1. Update the `source_dir` variable in the script with the path to your "Photos Library.photoslibrary" folder.
2. Update the `dest_dir` variable in the script with the path to your external, followed by the "ApplePhotosExport" folder.
3. Save the script as `copy_images.py`.
4. Open a terminal and navigate to the directory containing the script.
5. Run the script using the following command:

```bash
python copy_images.py
```
