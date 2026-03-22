import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def fix_css(html):
    patterns = [
        (r'(\.[a-z0-9-]+hero(?:-content)?\s*h1\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(2.4rem, 6vw, 4.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.[a-z0-9-]+hero-subtitle\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(1.4rem, 3.5vw, 2.5rem)\3\n      text-transform: uppercase;'),
    ]
    for pattern, repl in patterns:
        html = re.sub(pattern, repl, html, flags=re.IGNORECASE)
    
    if 'archinova-hero-content' in html:
        html = re.sub(r'(\.archinova-hero-content\s*\{[^}]*padding:\s*)([^;]+)(;)', r'\1 50px 40px\3', html)
        html = re.sub(r'(\.archinova-hero-content\s*\{[^}]*border:\s*)([^;]+)(;)', r'\1 3px solid var(--teal-dark)\3', html)
    
    return html

coordinator_map = {
    "VISIONVERSE": "Faculty Coordinator: Dr. Ayush Meena<br>Student Coordinators: Aditya Alaria & Aryan",
    "PROTOEXPO": "Faculty Coordinator: Mr. Mohit Kumar Tiwari<br>Student Coordinator: Santoshi Prajapat",
    "SKILLFORGE": "Non-Destructive Testing (NDT):<br>Faculty Coordinator: Dr. Santanu Malik<br>Student Coordinator: Shanvi (I Year)<br><br>Smart Construction using BIM:<br>Faculty Coordinators: Dr. Ayush Meena, Mr. Mohit Kumar Tiwari, and Dr. Siddharth<br>Student Coordinators: Yashashvi, Vanshika Shrimal, & Param",
    "BHAVISHYA": "Faculty Coordinator: Dr. Santanu Malik<br>Student Coordinators: Harshit Garg & Priyanshu Raj",
    "ARCHINOVA": "Faculty Coordinator: Ar. Garima Kotnala",
    "CONCRETE": "Faculty Coordinator: Mr. Prateek Sharma<br>Student Coordinators: Minakshi Nathawat & Gargi Sharma",
    "STRUCTOBRICK": "Faculty Coordinator: Dr. Vishal Singhal<br>Student Coordinators: Rahul Kumar (I Year), Aryan (I Year)",
    "CIVILIGENCE": "Faculty Coordinator: Mr. Prateek Sharma<br>Student Coordinator: Aryan (I Year)",
    "SYNERGY": "Faculty Coordinator: Mr. Sonu Kumar<br>Student Coordinator: Shanvi (I Year)",
    "TECHNOSCRIPT": "Faculty Coordinators: Dr. Mayank Gupta & Dr. Shilpi Jain<br>Student Coordinator: Mukesh (II Year)",
    "COMPRESSIVE": "Faculty Coordinator: Dr. Ayush Meena<br>Student Coordinators: Aditya Alaria & Aryan"
}

def fix_content(filename, html):
    h1_match = re.search(r'<h1>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    if not h1_match:
        return html
    
    h1_text = h1_match.group(1).upper()
    
    # Compressive Edge Specific Content Brute Force
    if "COMPRESSIVE EDGE" in h1_text or "ENGGCANVA" in h1_text:
        html = re.sub(r'<h1>.*?</h1>', r'<h1>Compressive Edge &ndash;<br>Cube Strength Challenge</h1>', html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r'<div class="section-teal-header" style="margin-top:0;">Overview</div>.*?<section class="engg-section">.*?</section>', 
                    r'<div class="section-teal-header" style="margin-top:0;">Overview</div>\n  <section class="engg-section">\n    <div class="engg-content">\n      <h3 class="teal-heading">Objective:</h3>\n      <p>Test the compressive strength of standard concrete cubes using a Compression Testing Machine (CTM) and compare the results with design specifications.</p>\n      <h3 class="teal-heading">Rules:</h3>\n      <ul class="engg-list">\n        <li>Standard 150mm x 150mm x 150mm concrete cubes must be provided/casted.</li>\n        <li>Testing will be performed as per IS 516 guidelines.</li>\n        <li>Evaluation based on achieved strength vs expected grade.</li>\n      </ul>\n    </div>\n  </section>', 
                    html, flags=re.DOTALL)

    # Coordinator Replacement in Hero
    matched_coord = None
    for key, val in coordinator_map.items():
        if key in h1_text:
            matched_coord = val
            break
    
    if matched_coord:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1' + matched_coord + r'\3', html, flags=re.DOTALL)

    # Strip Student Numbers Global (General patterns)
    html = re.sub(r'(Student Coordinator.*?)\s*[📞\[]\s*[\+\d -]{8,}[\]]?', r'\1', html, flags=re.IGNORECASE)
    
    # Strip from Footer specifically (handles multiple <p> tags)
    # Target: After "Student Coordinator</strong>"
    def strip_p_phones(match):
        content = match.group(0)
        # Strip phone numbers from any text within the block
        content = re.sub(r'📞\s*[\+\d -]{8,}', '', content)
        return content

    html = re.sub(r'<strong>Student Coordinator</strong>\s*(<p.*?</p>\s*)+', strip_p_phones, html, flags=re.DOTALL | re.IGNORECASE)

    return html

for filepath in html_files:
    fname = os.path.basename(filepath)
    if fname in ['index.html', 'Events.html', 'glimpse.html']:
        continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    html = fix_css(html)
    html = fix_content(fname, html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Final Robust Fix Applied.")
