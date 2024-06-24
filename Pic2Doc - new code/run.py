import datetime
import subprocess
import os

# Define the date to check against
deadline = datetime.datetime(2024, 7, 20)

# Get the current date
current_date = datetime.datetime.now()

# Check if the current date is before the deadline
if current_date < deadline:
    # Define the paths to file1.py and file2.py in the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1_path = os.path.join(current_dir, 'app.py')
    file2_path = os.path.join(current_dir, 'main.py')
    
    # Check if the files exist
    if os.path.exists(file1_path) and os.path.exists(file2_path):
        # Run file1.py
        subprocess.run(['python', file1_path])
        
        # Run file2.py
        subprocess.run(['python', file2_path])
    else:
        print(f"One or both files do not exist in {current_dir}.")
else:
    print("The current date is after the deadline. The scripts will not run.")
