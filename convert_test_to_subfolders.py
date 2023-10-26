import os
import shutil

# Path to the test folder containing sub-folders
test_folder = '/content/AML-1/Test'

# Path to the text files
class_file = 'classlabel.txt'
test_file = 'test.txt'

# Read sub-folders information from train.txt
subfolders_info = {}
with open(class_file, 'r') as file:
    for line in file:
        folder_name, folder_number = line.strip().split()
        subfolders_info[int(folder_number)] = folder_name

# Read image filenames and their corresponding folder numbers from test.txt
image_info = []
with open(test_file, 'r') as file:
    for line in file:
        filename, folder_number = line.strip().split()
        image_info.append((filename, int(folder_number)))

# Organize images into sub-folders
for filename, folder_number in image_info:
    folder_name = subfolders_info[folder_number]
    source_path = os.path.join(test_folder, filename)
    destination_folder = os.path.join(test_folder, folder_name)
    destination_path = os.path.join(destination_folder, filename)
    
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    # Move the image to the correct sub-folder
    shutil.move(source_path, destination_path)

print("Test images have been organized into sub-folders based on the class names.")
