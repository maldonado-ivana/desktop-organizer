# File Organizer Script

## Overview
This script organizes files within a specified folder into subfolders based on their file extensions. The script uses the 'os' and 'shut' modules. 

## Usage
1. Clone or download the script file to your local machine.
2. Open the script file and specify the target folder path in the `target_folder_path` variable.
3. Run the script by executing the following command in your terminal:
    ```
    python desktop-organizer.py
    ```
       
## Error Handling
The script includes error handling to improve user experience. It provides user-friendly messages indicating what went wrong.
   - `create_subfolder` Function:
     - Permission Errors: handles cases where the scrip lacks permissions to create a subfolder
     - File System Errors: deals with unexpected errors such as disk space issues and file system corruption
     - Invalid Path Errors: handles situations where the path of the parent folder is invalid or doesn't exist

## Important Note
Ensure that the target folder path specified in the script exists and is accessible. The script will not work if the folder path is invalid.

## Links to Documentation
- [Python official documentation: os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
- [Python official documentation: shutil — High-level file operations](https://docs.python.org/3/library/shutil.html)
