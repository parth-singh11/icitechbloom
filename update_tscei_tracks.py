import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    html = html.replace("Sustainable Civil Engineering", "Sustainable & Green Civil Eng")
    html = html.replace("Smart Infrastructure & Digital Construction", "Smart Infrastructure")
    # Climate-Resilient Infrastructure is already exact
    # Water Resources is already exact
    html = html.replace("AI/IoT in Civil Engineering", "AI/IoT Driven Civil Eng")
    # Interdisciplinary Solutions is already exact
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Finished TSCEI track texts")
