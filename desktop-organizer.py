import os #library to interact with the operating system
import shutil  #shutil library to move files

if __name__ == "__main__":
    print("Desktop Organizer Script")
    # path to downloads folder
    folder_path = '/PATH/TO/FOLDER'
    # validate whether folder path is a real path, if so run the clean funtion, esle return error message. 
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        # Need to write function to clean the folder
    else:
        print("Folder path is not valid. Please enter a valid folder path.")
        