import os
import time
from datetime import datetime, timedelta

def delete_old_files(directory, days):
    # Calculate the time threshold
    time_threshold = time.time() - days * 60 * 60 * 24

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the last modified time of the file
            file_mtime = os.path.getmtime(file_path)
            
            # If the file is older than the threshold, delete it
            if file_mtime < time_threshold:
                os.remove(file_path)
                print(f"Deleted {file_path}")

if __name__ == "__main__":
    directory = r"G:\My Drive\Backups\Bookmarks"
    days = 365  # Number of days
    delete_old_files(directory, days)