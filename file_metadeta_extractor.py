import os
import hashlib
import datetime

try:
    import exifread
    exif_available = True
except ImportError:
    exif_available = False

def get_file_info(file_path):
    if not os.path.exists(file_path):
        print("File not found.")
        return

    print("\n=== File Metadata ===")
    print(f"File Name      : {os.path.basename(file_path)}")
    print(f"File Size      : {os.path.getsize(file_path)} bytes")
    print(f"File Type      : {file_path.split('.')[-1]}")
    
    created_time = os.path.getctime(file_path)
    modified_time = os.path.getmtime(file_path)

    print("Created Time   :", datetime.datetime.fromtimestamp(created_time))
    print("Modified Time  :", datetime.datetime.fromtimestamp(modified_time))

    print("MD5 Hash       :", calculate_md5(file_path))

    if file_path.lower().endswith(('.jpg', '.jpeg')) and exif_available:
        extract_image_metadata(file_path)
    elif file_path.lower().endswith(('.jpg', '.jpeg')):
        print("\n[!] Install `exifread` to extract image metadata (pip install exifread).")

def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def extract_image_metadata(file_path):
    print("\n=== Image EXIF Metadata ===")
    with open(file_path, 'rb') as img_file:
        tags = exifread.process_file(img_file, stop_tag="UNDEF", details=False)

    if not tags:
        print("No EXIF metadata found.")
    else:
        for tag in tags:
            print(f"{tag:25}: {tags[tag]}")

def main():
    print(" ## ---  File Metadata Extractor --- ##")
    file_path = input("Enter the full path of the file: ").strip()
    file_path = os.path.expanduser(file_path)
    get_file_info(file_path)

if __name__ == '__main__':
    main()
