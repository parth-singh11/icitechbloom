import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def update_mayank_number(html):
    # Pattern to match Dr. Mayank Gupta and optionally some existing contact info or whitespace
    # We want to avoid duplicating if the number is already there
    if '70073295' in html:
        # Check if it's already correctly formatted next to his name
        pass
    
    # Simple replacement: look for his name and append the number if not present
    # Using a cautious regex to only match him as a name, not inside a tag or script if possible
    # But since he's always in <p> or <strong> or text, this is generally safe.
    
    # We'll use a negative lookahead to ensure we don't append if the number is already immediately following
    pattern = r'(Dr\.\s*Mayank\s*Gupta)(?!\s*📞\s*\+91-70073295)'
    replacement = r'\1 📞 +91-70073295'
    
    return re.sub(pattern, replacement, html)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = update_mayank_number(html)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {os.path.basename(filepath)}")

print("Global contact update complete.")
