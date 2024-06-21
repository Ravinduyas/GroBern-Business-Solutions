import pyautogui
import os
import time
from moviepy.editor import ImageSequenceClip

# Directory to save screenshots
output_dir = 'screenshots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Number of screenshots to take
num_screenshots = 10
# Interval between screenshots in seconds
interval = 1

# Take screenshots
for i in range(num_screenshots):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Save the screenshot to a file
    screenshot.save(f'{output_dir}/screenshot_{i}.png')
    # Wait for the specified interval
    time.sleep(interval)

# Frame rate for the video
fps = 1  # 1 frame per second

# Get a list of screenshot file paths
image_files = [os.path.join(output_dir, f'screenshot_{i}.png') for i in range(num_screenshots)]

# Create a video clip from the images
clip = ImageSequenceClip(image_files, fps=fps)

# Write the video file
clip.write_videofile('output_video.mp4', codec='libx264')
