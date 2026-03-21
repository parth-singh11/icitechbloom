import os
import glob

files = glob.glob('*.html')
for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('images/Screenshot 2026-03-18 203325.png', 'images/icimem.jpg')
    new_content = new_content.replace('images/regis.png', 'images/regis.jpg')
    new_content = new_content.replace('images/Screenshot 2026-03-18 201351.png', 'images/winprize.jpg')

    if new_content != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {p}")

print("Replacement complete.")
