import os #library to interact with the operating system
import shutil  #shutil library to move files

def create_subfolder_if_doesnt_exist(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name) # create the subfolder_path by joining the folder_path and subfolder_name
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def organize_folder(folder_path):
    for filename in os.listdir(folder_path): # loop through the files in the folder
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower() # get the file extension and cast it to lower case
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_doesnt_exist(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, subfolder_path) #method from shiutil library to move files
                print(f"Moved {filename} to {subfolder_path}")

if __name__ == "__main__":
    print("Desktop Organizer Script")
    # path to the folder to be cleaned
    target_folder_path = 'PATH_TO_FOLDER_TO_BE_CLEANED'
    # validate whether folder path is a real path, if so run the clean funtion, esle return error message. 
    if os.path.isdir(target_folder_path):
        organize_folder(target_folder_path)
    else:
        print("Folder path is not valid. Please enter a valid folder path.")
        