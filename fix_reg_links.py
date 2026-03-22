import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def update_reg_links(html):
    # Pattern to match <a> tags with "Register Now" or "REGISTER NOW" text
    # We want to change their href to "Events.html"
    
    # regex matches <a ... href="..." ...>Register Now</a>
    # We'll use a more flexible regex to find the href and replace it if the inner text is "Register Now"
    
    # First, let's normalize all href="events.html" to "Events.html" anyway
    html = html.replace('href="events.html"', 'href="Events.html"')
    html = html.replace("href='events.html'", 'href="Events.html"')
    
    # Now specifically target "Register Now" links
    # This pattern looks for <a> tags containing "Register Now" (ignoring tags inside)
    # and replaces the href.
    
    # We'll use a regex that handles the href attribute specifically within the a tag
    pattern = r'(<a[^>]*href=["\'])([^"\']*)(["\'][^>]*>\s*Register\s*Now\s*</a>)'
    replacement = r'\1Events.html\3'
    
    return re.sub(pattern, replacement, html, flags=re.IGNORECASE)

for filepath in html_files:
    # Skip Events.html itself if it has general registration buttons that shouldn't loop?
    # Actually, even on Events.html, "Register Now" usually points to the top or a form.
    # But the user said "every register now button should redirect to events.html".
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = update_reg_links(html)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated links in {os.path.basename(filepath)}")

print("Global registration link update complete.")
