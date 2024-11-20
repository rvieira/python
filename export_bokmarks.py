# This is the script that exports the bookmarks from the browser to a file
# The file is saved in a folder called "Bookmarks" in the directory defined by the variable "bookmarks_backup_path"
# The file is saved in the format "bookmarks_<date>.json"
# The bookmarks are saved in the JSON format
# The script is run by the command "python export_bookmarks.py"

import os
import json
from datetime import datetime
import shutil

# Define the path to the bookmarks backup folder
bookmarks_backup_path = r"G:\My Drive\Backups\Bookmarks"
now = datetime.now()
timestamp = now.strftime('%Y%m%d_%H%M%S')
bookmarks_file_name = "bookmarks_" + timestamp + ".json"
bookmarks_file_path = os.path.join(bookmarks_backup_path, bookmarks_file_name)

def export_bookmarks():
    # Get the bookmarks from the browser
    bookmarks = get_bookmarks()
    
    # Save the bookmarks to a file
    with open(bookmarks_file_path, 'w') as f:
        json.dump(bookmarks, f)
    
    print("Bookmarks exported to file: " + bookmarks_file_path)

def get_bookmarks():
    # Get the bookmarks from the Chrome browser
    # The bookmarks will be returned in a JSON format
    pass
    # Path to the Chrome bookmarks file
    chrome_bookmarks_path = os.path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default\Bookmarks"
    
    # Read the bookmarks file
    with open(chrome_bookmarks_path, 'r', encoding='utf-8') as f:
        bookmarks_data = json.load(f)
    
    # Extract the bookmarks
    bookmarks = bookmarks_data.get('roots', {}).get('bookmark_bar', {}).get('children', [])
    
    return bookmarks

if __name__ == "__main__":
    export_bookmarks()
