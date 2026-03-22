import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def fix_contact_layout_v2(html):
    # Fix the missing </p> from previous run
    # Pattern to match the current broken state:
    # <p ...>Dr. Mayank Gupta \n <p ...>Assistant Professor, PCE</p>
    
    # We'll just look for Dr. Mayank Gupta followed by a <p tag without a closing </p>
    pattern = r'(<p[^>]*>)\s*Dr\.\s*Mayank\s*Gupta\s*(\n\s*<p[^>]*>)\s*Assistant\s*Professor,\s*PCE\s*</p>'
    replacement = r'\1Dr. Mayank Gupta</p>\2Assistant Professor, PCE</p>'
    
    return re.sub(pattern, replacement, html, flags=re.MULTILINE)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = fix_contact_layout_v2(html)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Corrected HTML in {os.path.basename(filepath)}")

print("Contact layout tag fix complete.")
