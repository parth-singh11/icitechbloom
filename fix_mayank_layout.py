import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def fix_contact_layout(html):
    # Pattern to match Mayank's current messed up block
    # Match Dr. Mayank Gupta + Number followed by Assistant Professor
    # Using re.DOTALL to handle multiline if needed, but they are usually adjacent lines
    
    # regex matches:
    # 1. <p ...>Dr. Mayank Gupta 📞 +91-70073295</p>
    # 2. whitespace
    # 3. <p ...>Assistant Professor, PCE</p>

    pattern = r'(<p[^>]*>)\s*Dr\.\s*Mayank\s*Gupta\s*📞\s*\+91-70073295\s*</p>(\s*<p[^>]*>)\s*Assistant\s*Professor,\s*PCE\s*</p>'
    
    # Replacement for Mayank (moving number to bottom line like his colleagues)
    # Re-using the first p tag style for the name and second p tag style for designation
    replacement = r'\1Dr. Mayank Gupta\2Assistant Professor, PCE</p>\n              <p style="font-size: 0.85rem;">📞 +91-70073295</p>'
    
    return re.sub(pattern, replacement, html, flags=re.MULTILINE)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = fix_contact_layout(html)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Fixed Layout in {os.path.basename(filepath)}")

print("Contact layout fix complete.")
