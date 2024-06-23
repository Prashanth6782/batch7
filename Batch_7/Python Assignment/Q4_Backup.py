import os
import shutil
from datetime import datetime
import sys

def backup_config(spath, tpath):
    #check if the sopurce and target path exists

    if not os.path.exists(spath):
        print(f"Error: Source directory '{spath}' does not exist.")
        return
   
    if not os.path.exists(tpath):
        print(f"Error: Target directory '{tpath}' does not exist.")
        return

    # Get list of files in source directory
    files = os.listdir(spath)

    #backup the files
    for file_name in files:
        source_file_path = os.path.join(spath, file_name)
        if os.path.isfile(source_file_path):
            dest_file_path = os.path.join(tpath, file_name)
            
            # Check if file exists in destination directory
            if os.path.exists(dest_file_path):
                # Append timestamp to file name
                base_name, ext = os.path.splitext(file_name)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                new_file_name = f"{base_name}_{timestamp}{ext}"
                dest_file_path = os.path.join(tpath, new_file_name)
            
            # Copy file to destination directory
            try:
                shutil.copy2(source_file_path, dest_file_path)
                print(f"Copied '{source_file_path}' to '{dest_file_path}'")
            except Exception as e:
                print(f"Error copying '{source_file_path}' to '{dest_file_path}': {e}")

# Example usage:
def main():
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        return
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    backup_config(source_dir, dest_dir)

if __name__ == "__main__":
    main()
