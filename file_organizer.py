import os
import shutil
from datetime import datetime
import re

fileFormat = {
    "Web": [".html5", ".html", ".htm", ".xhtml"], 
    "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"], 
    "Video": [".avi", ".log", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"], 
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
                 ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"], 
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"], 
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"]
}

def check_path_validation(prompt):
    while True:
        try:
            path = input(prompt).strip()  # Remove any surrounding spaces
            if os.path.exists(path):
                return path
            else:
                print(f"The directory {path} does not exist. Please provide a valid path.")
        except KeyboardInterrupt:
            print("\nOperation interrupted. Exiting...")
            exit(1)

def log_report(working_dir):
    sanitized_name = re.sub(r'[<>:"/\\|?*]', '_', working_dir)
    report_file = os.path.join(log_path, f"{sanitized_name}.log")
    if not os.path.exists(report_file):
        open(report_file, "x").close()    
    with open(report_file, "a")as report:
        for log in logs:
            report.write(f"{log}.\n")
  
def file_rename(path , file):
    if not os.path.isfile(path):
        logs.append(f"{datetime.now()} | file name did not change {path}")
        return
    timestamp = os.path.getctime(path)
    date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')    
    name, extension = os.path.splitext(file)
    new_name = f"{name}_{date_str}{extension}"
    new_path = os.path.join(dir_path, new_name)
    counter = 1
    while os.path.exists(new_path):
        new_name = f"{name}_{date_str}_{counter}{extension}"
        new_path = os.path.join(dir_path, new_name)
        counter += 1          
    os.rename(path, new_path)
    logs.append(f"{datetime.now()} | Renamed: {file} -> {new_name}")
    return new_path
    
              
def file_move(source_path, file):
    if not os.path.isfile(source_path):
        logs.append(f"{datetime.now()} | MOVE: couldnt find {source_path}")
        return 
    extension = os.path.splitext(file)[1]
    for category, extensions in fileFormat.items():
        if extension in extensions:
            destination_path = os.path.join(dir_path, category)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.move(source_path, os.path.join(destination_path, file))   
            logs.append(f"{datetime.now()} | Moved: {file} -> {destination_path}")
            return
    logs.append(f"{datetime.now()} | MOVE: No matching category for {file}")

    
log_path = check_path_validation("Enter path to store log file: ")
if not os.path.exists(log_path):
    os.makedirs(log_path)
dir_path = check_path_validation("Enter path to working directory: ")
dir_content = os.listdir(dir_path)
logs = []

for category in fileFormat:
    subdir_path = os.path.join(dir_path, category)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)
        logs.append(f"{datetime.now()} | Directory: '{os.path.basename(subdir_path)}' created at:\n {subdir_path}")
    else:
        logs.append(f"{datetime.now()} | Directory: '{os.path.basename(subdir_path)}' already exists at:\n {subdir_path}")

print("\nStarting renaming process.")
try:
    for file in dir_content:
        file_path = os.path.join(dir_path, file) 
        if not os.path.isfile(file_path) or file.startswith('.'):
            logs.append(f"{datetime.now()} | Skipping: {file} because it doesnt match with the requierments.")
            continue
        new_file_path = file_rename(file_path, file)
        file_move(new_file_path, os.path.basename(new_file_path))
    working_dir_name = os.path.basename(dir_path)
    log_report(working_dir_name)
    print("Organizing directory and Reporting process finished successfully.")
except Exception as e:
    print(f"Error while organizing files: {e}")     
