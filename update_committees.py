import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Accordion Co-Convener
    accordion_target = '''<p><strong>Mr. Mohit Kumar Tiwari</strong><br>Assistant Professor, Civil Engg., PCE</p>
              <p><strong>Mr. Prateek Sharma</strong><br>Assistant Professor, Civil Engg., PCE</p>'''
    accordion_replacement = '''<p><strong>Dr. Mayank Gupta</strong><br>Assistant Professor, Civil Engg., PCE</p>
              <p><strong>Mr. Mohit Kumar Tiwari</strong><br>Assistant Professor, Civil Engg., PCE</p>
              <p><strong>Mr. Prateek Sharma</strong><br>Assistant Professor, Civil Engg., PCE</p>'''
    content = content.replace(accordion_target, accordion_replacement)

    # 2. Footer Co-Convener (Style 1 - as in Events.html)
    footer_target_1 = '''<div class="contact-item-grid">
            <div>
              <p style="font-size: 0.95rem; margin-bottom: 4px;">Mr. Mohit Kumar Tiwari</p>'''
              
    footer_replacement_1 = '''<div class="contact-item-grid">
            <div>
              <p style="font-size: 0.95rem; margin-bottom: 4px;">Dr. Mayank Gupta</p>
              <p style="font-size: 0.85rem; color: #555;">Assistant Professor, PCE</p>
            </div>
            <div>
              <p style="font-size: 0.95rem; margin-bottom: 4px;">Mr. Mohit Kumar Tiwari</p>'''

    content = content.replace(footer_target_1, footer_replacement_1)
    
    # 3. Footer Co-Convener (Style 2 - as in index.html)
    footer_target_2 = '''<div class="contact-item-grid" style="gap: 16px;">
            <div>
              <p style="font-size: 0.95rem; margin-bottom: 4px; white-space: nowrap; color: #333;">Mr. Mohit Kumar Tiwari</p>'''
              
    footer_replacement_2 = '''<div class="contact-item-grid" style="gap: 16px;">
            <div>
              <p style="font-size: 0.95rem; margin-bottom: 4px; white-space: nowrap; color: #333;">Dr. Mayank Gupta</p>
              <p style="font-size: 0.85rem; color: #555; margin-bottom: 2px;">Assistant Professor, PCE</p>
            </div>
            <div>
              <p style="font-size: 0.95rem; margin-bottom: 4px; white-space: nowrap; color: #333;">Mr. Mohit Kumar Tiwari</p>'''

    content = content.replace(footer_target_2, footer_replacement_2)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done appending Dr. Mayank Gupta to Co-Conveners.')
