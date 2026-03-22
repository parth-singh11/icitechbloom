import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def surgical_cleanup(html):
    # Task 1: Contact Number Correction
    # Replace +91-70073295 with +91-[7007329509]
    # Note: Explicitly using brackets as requested by user
    html = html.replace('+91-70073295', '+91-[7007329509]')
    
    # Task 2: Purge "Ghost" Links (Compressive Edge)
    # 1. Remove <li> containing the link (common in dropdowns)
    li_pattern = r'<li>\s*<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?</a>\s*</li>'
    html = re.sub(li_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Remove <a> links directly (common in mobile nav or grids)
    a_pattern = r'<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?</a>'
    html = re.sub(a_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Handle cases where &nbsp; or other spacing might be present in mobile nav
    mobile_pattern = r'<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?—\s*Compressive\s*Edge\s*</a>'
    html = re.sub(mobile_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)

    return html

def verify_links(html, filename):
    synergy = len(re.findall(r'synergy-greenscape\.html', html, re.I))
    ball_smash = len(re.findall(r'ball-smash\.html', html, re.I))
    glimpse = len(re.findall(r'glimpse\.html', html, re.I))
    compressive = len(re.findall(r'Compressive Edge', html, re.I))
    return synergy, ball_smash, glimpse, compressive

for filepath in html_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = surgical_cleanup(html)
    s, b, g, c = verify_links(new_html, fname)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Fixed: {fname} (Synergy: {s}, BallSmash: {b}, Glimpse: {g}, CompressiveLeft: {c})")
    else:
        print(f"No changes: {fname} (Synergy: {s}, BallSmash: {b}, Glimpse: {g}, CompressiveLeft: {c})")

print("Surgical cleanup complete.")
