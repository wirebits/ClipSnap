#ClipSnap
#A tool which records the copied images of the clipboard.
#Author - Wirebits

import os
import sys
import time
from PIL import ImageGrab
from datetime import datetime

folder_name = "Clipboard Images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

image_count = 1

while True:
    current_time = datetime.now()
    clipboard_image = ImageGrab.grabclipboard()
    timestamp = current_time.strftime("%d-%m-%y_%H_%M_%S")
    
    if clipboard_image:
        image_name = os.path.join(folder_name, f"image{image_count}_{timestamp}.png")
        clipboard_image.save(image_name)
        image_count += 1
    else:
        sys.exit()
    time.sleep(1)
