import os
import shutil

# Path to the folder containing training images
source_folder = 'content/train'

# Loop through each image in the source folder
for filename in os.listdir(source_folder):
    # Extract class name from the filename (assuming the class name is the part before the last two underscores)
    class_name = '_'.join(filename.split('_0')[:-1])

    # Create a destination folder if it doesn't exist
    destination_folder = os.path.join(source_folder, class_name)
    os.makedirs(destination_folder, exist_ok=True)

    # Move the image to the corresponding class folder
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
    shutil.move(source_path, destination_path)

print("Images have been organized into folders based on class names.")
