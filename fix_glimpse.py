import os
import glob

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # The link in navbar originally was "Glimpse of ICI TechBloom 25"
    # It might have been replaced to "Glimpse of ICI TechBloom 26"
    html = html.replace(">Glimpse of ICI TechBloom 26</a>", ">Glimpse of ICI TechBloom 25</a>")
    html = html.replace('alt="Glimpse of ICI TechBloom 26"', 'alt="Glimpse of ICI TechBloom 25"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed Glimpse links")
