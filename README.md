# Automation Scripts for File Management

## Overview
This repository contains two Python scripts for automating file management tasks:
1. **File Organizer**: Categorizes and renames files in a specified directory.
2. **Backup Script**: Creates a timestamped backup of a specified directory.

---

## Scripts

### File Organizer
- **Path**: `file_organizer.py`
- **Description**: Organizes files by categories (e.g., documents, images) and renames them with timestamps.
- **Usage**: 
  - Run the script.
  - Provide the path to the working directory when prompted.
  - Logs are generated in the `logs` folder.

### Backup Script
- **Path**: `backup_script.py`
- **Description**: Creates a timestamped copy of a specified directory.
- **Usage**: 
  - Run the script.
  - Provide the source directory when prompted.

---

## Getting Started

Follow these steps to set up and use the scripts in this repository:

### Prerequisites
- Ensure you have Python 3.8 or higher installed on your system.
- Clone the repository to your local machine.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
2. Navigate to the project directory
   ```bash
   cd <repository_name>
3. Install dependencies
   ```bash
   git clone <repository_url>

### Usage

#### File Organizer Script
To organize files into categorized subdirectories:

1. Run the organizer script:
   ```bash
   python automatic_file_organizer.py
2. Enter the path to the working directory when prompted.
3. The script will:
   - Categorize files into subdirectories such as Web, Pictures, Videos, etc.
   - Rename files with their creation date to avoid duplication.
   - Log operations in the `logs` folder.   

---

## Backup Script

The backup script creates a backup of a specified directory and compresses it with a timestamp.

### Usage

1. Modify the `source_directory` variable with the directory you want to back up.
2. Run the script, and it will create a backup in the format:
   `original_directory_backup_YYYYMMDD_HHMMSS`.