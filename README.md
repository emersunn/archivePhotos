# Archive Photos

This Python script copies image files from Photos.app to a destination directory, renaming them sequentially as image1, image2, image3, and so on.

## Why?

I don't trust Photos.app built-in export, if you are not careful you could end up with inferior jpegs. My method may be faster, but I have not tested it. I have 50GB of photos and it went pretty quick.

## Requirements

- Python 3.6 or higher
- Local drive large enough to hold your Photos library. 
- External drive large enough to handle the export. 

## Prior to use 

- Make sure your photo library is up-to-date. In Photos.app go to Settings → iCloud → Download originals to this Mac. 
- While still in Photos.app, click on Library → All Photos to check the download progres. Progress shows at the bottom of the window.
- Once all photos are downloaded execute the script. 

## Usage

1. Update the `source_dir` variable in the script with the path to your "Photos Library.photoslibrary" folder.
2. Update the `dest_dir` variable in the script with the path to your external drive.
3. Save the script as `copy_images.py`.
4. Open a terminal and navigate to the directory containing the script.
5. Run the script using the following command:

```bash
python copy_images.py
```
## After use

- Be sure revert the preferences in Settings → iCloud → Optimize Mac Storage if you need to save space.
