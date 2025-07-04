# File Metadata Extractor

A simple Python tool to extract and display important metadata from any file, including file size, timestamps, file type, and MD5 hash. If the file is a JPEG image, it can also extract EXIF metadata (e.g., camera model, timestamp) using the `exifread` library.

This tool can be useful in digital forensics for checking file integrity, verifying timestamps, and detecting image tampering.

---

## Features

- Extracts file name, size, type, creation and modification times
- Computes the MD5 hash of any file
- Extracts EXIF metadata from `.jpg` and `.jpeg` images
- Works with all file types (text, documents, images, executables, etc.)
- Gracefully handles missing files or missing EXIF library

---

## Requirements

- Python 3.x
- Optional: `exifread` library for JPEG metadata

To install the EXIF library:

```bash
pip install exifread
```
## How to Use

- Clone the repository:

```bash
git clone https://github.com/niklaus2811000/file-metadata-extractor.git
cd file-metadata-extractor
```
- Run the script:

```bash
python3 file_metadata_extractor.py
```
When prompted, enter the full path to the file you want to analyze. Example:

```bash
Enter the full path of the file: /Users/ayn/Desktop/IMG_0826.PNG
```

## The tool will display:

- File name and type
- Size (in bytes)
- Created and modified timestamps
- MD5 hash
- Optional: EXIF metadata (for JPEG images)

## Example Output
```bash
ayn@MacBook-Air python % /usr/local/bin/python3 "/Users/ayn/Documents/python/Extract Metadata/file_metadata_extractor.py"
 ## ---  File Metadata Extractor --- ##
Enter the full path of the file: /Users/ayn/Desktop/IMG_0826.PNG

=== File Metadata ===
File Name      : IMG_0826.PNG
File Size      : 3438116 bytes
File Type      : PNG
Created Time   : 2025-05-14 14:25:51.686111
Modified Time  : 2025-05-14 14:21:49
MD5 Hash       : 29f32f31ee9e508c6459068e1855cb97
```



