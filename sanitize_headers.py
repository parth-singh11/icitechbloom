import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
files_to_fix = ['SkillForge.html', 'synergy-greenscape.html', 'ArchiNova  Designing Tomorrow.html']

def sanitize_css(html):
    # Fix box width and spacing
    html = re.sub(r'(\.archinova-hero-content\s*\{[^}]*max-width:\s*)(900px)(;)', r'\1 1000px\3', html)
    
    # Fix H1 and cleanup duplicates
    h1_block_pattern = r'(\.archinova-hero-content\s*h1\s*\{)(.*?)(\})'
    def clean_h1(match):
        header = match.group(1)
        content = match.group(2)
        footer = match.group(3)
        # Force the clamp and remove duplicates
        content = re.sub(r'font-size:\s*[^;]+;', 'font-size: clamp(1.8rem, 4.5vw, 2.8rem);', content)
        content = re.sub(r'text-transform:\s*uppercase;(\s*text-transform:\s*uppercase;)+', 'text-transform: uppercase;', content)
        return header + content + footer

    html = re.sub(h1_block_pattern, clean_h1, html, flags=re.DOTALL)

    # Fix Subtitle and cleanup duplicates
    sub_block_pattern = r'(\.archinova-hero-subtitle\s*\{)(.*?)(\})'
    def clean_sub(match):
        header = match.group(1)
        content = match.group(2)
        footer = match.group(3)
        content = re.sub(r'text-transform:\s*uppercase;(\s*text-transform:\s*uppercase;)+', 'text-transform: uppercase;', content)
        return header + content + footer

    html = re.sub(sub_block_pattern, clean_sub, html, flags=re.DOTALL)
    
    return html

for fname in files_to_fix:
    filepath = os.path.join(base_dir, fname)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        html = sanitize_css(html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Headers Sanitized to 2.8rem and 1000px width.")
