import os
import glob
import re

dir_path = r"c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom"
html_files = glob.glob(os.path.join(dir_path, "*.html"))

glimpse_file = os.path.join(dir_path, "glimpse.html")

with open(glimpse_file, "r", encoding="utf-8") as f:
    glimpse_content = f.read()

# Extract the footer from glimpse.html
footer_match = re.search(r'<footer class="site-footer">.*?</footer>', glimpse_content, re.DOTALL)
if not footer_match:
    print("Error: Could not find footer in glimpse.html")
    exit(1)

glimpse_footer = footer_match.group(0)

for file in html_files:
    if os.path.basename(file) == "glimpse.html":
        continue
    
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the existing footer with the one from glimpse.html
    new_content = re.sub(r'<footer class="site-footer">.*?</footer>', glimpse_footer.replace('\\', '\\\\'), content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file)}")

print("Done")
