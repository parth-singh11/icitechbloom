import os
import glob
import re

dir_path = r"c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom"
html_files = glob.glob(os.path.join(dir_path, "*.html"))

# 1. CSS changes
css_file = os.path.join(dir_path, "responsive.css")
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

if ".nav-links { justify-content: flex-end; }" not in css_content:
    css_content += "\n\n/* Added for header alignment */\n.nav-links { justify-content: flex-end !important; }\n"
    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated responsive.css")

# 2. HTML changes
nav_brand_pattern = re.compile(
    r'<div class="nav-brand">\s*'
    r'<!-- ICI TechBloom logo \+ name -->\s*'
    r'<div class="nav-college-logos">\s*'
    r'<img src="([^"]+)" alt="([^"]+)" style="([^"]+)">\s*'
    r'</div>\s*'
    r'<span class="nav-brand-text">([^<]+)</span>\s*'
    r'</div>', re.MULTILINE
)

nav_brand_replacement = (
    r'<a href="index.html" class="nav-brand">\n'
    r'      <!-- ICI TechBloom logo + name -->\n'
    r'      <div class="nav-college-logos">\n'
    r'        <img src="\1" alt="\2" style="\3">\n'
    r'      </div>\n'
    r'      <span class="nav-brand-text">\4</span>\n'
    r'    </a>'
)

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # Replace nav-brand
    content = nav_brand_pattern.sub(nav_brand_replacement, content)
    
    # Remove ICI TechBloom link from desktop nav
    # sometimes active class, sometimes not, sometimes spaces inside
    content = re.sub(r'\s*<li><a href="index\.html"[^>]*>ICI TechBloom</a></li>', '', content)
    
    # Remove About link from desktop nav
    content = re.sub(r'\s*<li><a href="About\.html"[^>]*>About</a></li>', '', content)
    
    # Remove ICI TechBloom link from mobile nav
    content = re.sub(r'\s*<a href="index\.html"[^>]*>ICI TechBloom</a>', '', content)
    
    # Remove About link from mobile nav
    content = re.sub(r'\s*<a href="About\.html"[^>]*>About</a>', '', content)
    
    if content != original_content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file)}")

print("Done")
