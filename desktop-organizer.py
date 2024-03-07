import os #library to interact with the operating system
import shutil  #module to move files

def create_subfolder(parent_folder_path, subfolder_name):
    """
    Creates a subfolder within the specified parent folder if it doesn't already exist.
    
    Args:
        parent_folder_path: Path of the parent folder.
        subfolder_name: Name of the subfolder to be created.
    
    Returns:
        str: Path of the created subfolder.
    """
    subfolder_path = os.path.join(parent_folder_path, subfolder_name)
    try:
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        return subfolder_path
    except OSError as e:
        print(f"Error creating subfolder: {e}")
        return None
    

def organize_files_by_extension(folder_path):
    """
    Organizes files within the specified folder into subfolders based on their file extensions.
    
    Args:
        folder_path: Path of the folder to organize.
    """
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, subfolder_path)
                print(f"Moved {filename} to {subfolder_path}")

if __name__ == "__main__":
    print("Desktop Organizer Script")
    target_folder_path = 'PATH_TO_FOLDER_TO_BE_CLEANED' # Provide path to the folder to organize
    if os.path.isdir(target_folder_path):
        organize_files_by_extension(target_folder_path)
    else:
        print("Folder path is not valid. Please enter a valid folder path.")
    