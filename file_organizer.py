import os
from datetime import datetime

# "C:/Users/97250/DevOps/testing_organized_content"
def organize_in_place():
    logs = []
    try:
        if not os.path.isdir(unorganized_dir):
            print(f"The path {unorganized_dir} is not a directory.")
            return
        dir_content = os.listdir(unorganized_dir)
        print(f"Processing files in {unorganized_dir}")
        for file in dir_content:
            file_path = os.path.join(unorganized_dir, file)
            if os.path.isdir(file_path) or file.startswith('.'):
                print(f"Skipping hidden file or directory: {file}")
                continue
            #reg files process
            timestamp = os.path.getctime(file_path)
            date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            name, extension = os.path.splitext(file)
            prefix = extension.lstrip('.')
            new_name = f"{prefix}_{name}_{date_str}{extension}"
            new_path = os.path.join(unorganized_dir, new_name)
            #renaming
            os.rename(file_path, new_path)           
            print(f"{file}: renamed successfully")
            logs.append(f"{datetime.now()} | Renamed: {file} -> {new_name}")
        log_report(unorganized_dir, logs)    
    except Exception as e:
        print(f"Error while organizing files: {e}")

#loger
def log_report(directory, logs):
    report_path = os.path.join(directory, "organized_report.txt")
    with open(report_path, "w") as report:
        for log in logs:
            report.write(log + "\n")
    print("Report generated successfully")        


unorganized_dir = input("Enter path to directory you want to organize: ")
if os.path.exists(unorganized_dir):
    organize_in_place()
else:
    print(f"The directory {unorganized_dir} does not exist.")