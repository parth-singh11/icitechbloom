import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def surgical_cleanup(html):
    # Task 1: Contact Number Correction
    # Replace +91-70073295 with +91-[7007329509]
    html = html.replace('+91-70073295', '+91-[7007329509]')
    
    # Task 2: Purge "Ghost" Links (Compressive Edge)
    # 1. Remove <li> containing the link
    # Pattern handles whitespace and various quote styles
    li_pattern = r'<li>\s*<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?</a>\s*</li>'
    html = re.sub(li_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Remove <a> links directly if not in <li>
    a_pattern = r'<a[^>]*href=["\']Compressive\s*Edge\s*-\s*Cube\s*Strength\s*Challenge\.html["\'][^>]*>.*?</a>'
    html = re.sub(a_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Specifically look for dropdown items or text mentions in lists
    # Sometimes they are in mobile menus without specific <li> wrappers if they are just <a>
    
    # 4. Remove from Events.html grid (if it exists)
    # The grid usually looks like <div class="event-card"> or <li> with the link
    # I'll look for any block that contains the link and might be a card
    # Usually event cards have a specific class.
    
    return html

def verify_links(html, filename):
    synergy = len(re.findall(r'synergy-greenscape\.html', html, re.I))
    ball_smash = len(re.findall(r'ball-smash\.html', html, re.I))
    glimpse = len(re.findall(r'glimpse\.html', html, re.I))
    return synergy, ball_smash, glimpse

for filepath in html_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = surgical_cleanup(html)
    s, b, g = verify_links(new_html, fname)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Fixed: {fname} (Synergy: {s}, BallSmash: {b}, Glimpse: {g})")
    else:
        print(f"No changes: {fname} (Synergy: {s}, BallSmash: {b}, Glimpse: {g})")

print("Surgical cleanup complete.")
