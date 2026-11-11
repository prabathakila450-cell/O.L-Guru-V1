import os
import shutil

list_file = "all_files_list.txt"
storage_dir = "./.git_batches"

if not os.path.exists(storage_dir):
    os.makedirs(storage_dir)

with open(list_file, "r") as f:
    files = [line.strip() for line in f.readlines()]

# Keep first 90, move the rest
to_hide = files[90:]

for file_path in to_hide:
    if os.path.exists(file_path):
        # Create destination path in storage_dir preserving structure
        # Strip leading ./
        rel_path = file_path.lstrip("./")
        dest_path = os.path.join(storage_dir, rel_path)
        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        try:
            shutil.move(file_path, dest_path)
        except Exception as e:
            print(f"Error moving {file_path}: {e}")
