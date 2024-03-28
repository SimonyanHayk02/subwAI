import os

def rename_png_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Iterate over each file
    for file in files:
        # Check if the file is a PNG file
        if not file.endswith('.png'):
            directory_path = 'images/training'+f'/{file}'
            rename_png_files(directory=directory_path)
        elif file.endswith('.png'):
            # Extract file extension
            file_name, file_extension = os.path.splitext(file)
            
            # Rename the file by adding "_new" before the extension
            new_file_name = f'{int(file_name) + 1500}' + file_extension
            
            # Construct old and new file paths
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed {file} to {new_file_name}')

# Replace 'directory_path' with the path to your directory containing PNG files
directory_path = 'images/training'
rename_png_files(directory_path)

