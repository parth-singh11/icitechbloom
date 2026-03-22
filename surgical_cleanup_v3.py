import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def surgical_cleanup(html):
    # Task 1: Contact Number Correction
    html = html.replace('+91-70073295', '+91-[7007329509]')
    
    # Task 2: Purge "Ghost" Links (Compressive Edge)
    # 1. Remove <li> containing the link
    li_pattern = r'<li>\s*<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?</a>\s*</li>'
    html = re.sub(li_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Remove <a> links directly
    a_pattern = r'<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?</a>'
    html = re.sub(a_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Remove <tr> containing "Compressive Edge" in tables
    tr_pattern = r'<tr>\s*<td>\s*Compressive\s*Edge.*?\s*</td>.*?</tr>'
    html = re.sub(tr_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)

    return html

for filepath in html_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = surgical_cleanup(html)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Fixed: {fname}")

print("Surgical cleanup complete.")
