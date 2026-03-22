import os
import glob

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = html.replace('+91-[7007329509]', '+91-7007329509')
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Removed brackets in {os.path.basename(filepath)}")

print("Bracket removal complete.")
