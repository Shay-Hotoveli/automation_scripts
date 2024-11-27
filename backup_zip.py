# source_directory C:/Users/97250/DevOps/testing_organized_files

import os
import shutil
from datetime import datetime

def backup_directory(source_dir):
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = f"{source_dir}_backup_{timestamp}"

    try:
        shutil.copytree(source_dir, backup_dir)
        print(f"Backup directory created successfully: {backup_dir}")
    except Exception as e:
        print(f"Error during backup: {e}")
        return

    # Optional: Compress the backup
    '''compressed_backup = shutil.make_archive(backup_dir, 'zip', backup_dir)
    print(f"Compressed backup created: {compressed_backup}")'''


if __name__ == "__main__":
    source_directory = input("Enter the path to the directory you want to back up: ").strip()
    backup_directory(source_directory)