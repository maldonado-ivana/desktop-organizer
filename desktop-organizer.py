import os #library to interact with the operating system
import shutil  #shutil library to move files


if __name__ == "__main__":
    print("Desktop Organizer Script")
    # path to the folder to be cleaned
    target_folder_path = 'PATH_TO_FOLDER_TO_BE_CLEANED'
    # validate whether folder path is a real path, if so run the clean funtion, esle return error message. 
    if os.path.isdir(folder_path):
        clean_folder(folder_path) 
        # NEED TO CREATE CLEAN FOLDER FUNCTION
    else:
        print("Folder path is not valid. Please enter a valid folder path.")
        