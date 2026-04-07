import os
import shutil



def preview_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    categories = {
        "jpg": "Images",
        "jpeg": "Images",
        "png": "Images",
        "gif": "Images",
        "bmp": "Images",
        "webp": "Images",

        "pdf": "Documents",
        "txt": "Documents",
        "doc": "Documents",
        "docx": "Documents",
        "ppt": "Documents",
        "pptx": "Documents",
        "xls": "Documents",
        "xlsx": "Documents",
        "csv": "Documents",

        "mp4": "Videos",
        "mov": "Videos",
        "avi": "Videos",
        "mkv": "Videos",

        "mp3": "Audio",
        "wav": "Audio",
        "m4a": "Audio",

        "zip": "Archives",
        "rar": "Archives",
        "7z": "Archives"
    }

    summary = {}

    for file in files:
        name, extension = os.path.splitext(file)
        extension = extension.replace(".", "").lower()
        if extension == "":
            category = "Others"
        else:
            category = categories.get(extension, "Others")
        
        summary[category] = summary.get(category, 0) + 1
    return(summary)

def sort_files(folder_path):
    moved_count = 0
    skipped_files = []
    renamed_count = 0
    # folder_path = "/Users/macbook/Downloads/Test_Folder"
    
    # complete_list = os.listdir() #For all folders and files in the current directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))] #For all folders and files in the current directory

    # for list in complete_list:
    #     print(list)
    categories = {
        "jpg": "Images",
        "jpeg": "Images",
        "png": "Images",
        "gif": "Images",
        "bmp": "Images",
        "webp": "Images",

        "pdf": "Documents",
        "txt": "Documents",
        "doc": "Documents",
        "docx": "Documents",
        "ppt": "Documents",
        "pptx": "Documents",
        "xls": "Documents",
        "xlsx": "Documents",
        "csv": "Documents",

        "mp4": "Videos",
        "mov": "Videos",
        "avi": "Videos",
        "mkv": "Videos",

        "mp3": "Audio",
        "wav": "Audio",
        "m4a": "Audio",

        "zip": "Archives",
        "rar": "Archives",
        "7z": "Archives"
    }
    for file in files:
        # print(file)
        name, extension = os.path.splitext(file)
        # print(f"Name: {name}")
        # print(f"Extension: {extension}")
        extension = extension.replace('.','')
        extension = extension.lower()
        if extension == '':
            skipped_files.append(file)
            continue
        # destination_folder = os.path.join(folder_path, extension)
        category = categories.get(extension, "Others")
        destination_folder = os.path.join(folder_path, category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # To move files into folders
        source = os.path.join(folder_path, file)
        destination = os.path.join(destination_folder, file)
        if os.path.exists(destination):
            renamed_count += 1
            counter = 1
            name, ext = os.path.splitext(file)
            while(os.path.exists(destination)):
                new_name = f"{name}_{counter}{ext}"
                destination = os.path.join(destination_folder, new_name)
                counter += 1

        shutil.move(source, destination)
        moved_count += 1
    
    return moved_count, skipped_files, renamed_count

    print("Files organised succesfully.")