import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

coordinators = {
    "VisionVerse": {
        "faculty": "Dr. Ayush Meena",
        "students": "Aditya Alaria & Aryan"
    },
    "ProtoExpo": {
        "faculty": "Mr. Mohit Kumar Tiwari",
        "students": "Santoshi Prajapat"
    },
    "SkillForge": {
        "NDT": {
            "faculty": "Dr. Santanu Malik",
            "student": "Shanvi (I Year)"
        },
        "BIM": {
            "faculty": "Dr. Ayush Meena, Mr. Mohit Kumar Tiwari, and Dr. Siddharth",
            "students": "Yashashvi, Vanshika Shrimal, & Param"
        }
    },
    "Bhavishya": {
        "faculty": "Dr. Santanu Malik",
        "students": "Harshit Garg & Priyanshu Raj"
    },
    "ArchiNova": {
        "faculty": "Ar. Garima Kotnala",
        "students": None
    },
    "ConcreTech": {
        "faculty": "Mr. Prateek Sharma",
        "students": "Minakshi Nathawat & Gargi Sharma"
    },
    "StructoBrick": {
        "faculty": "Dr. Vishal Singhal",
        "students": "Rahul Kumar (I Year), Aryan (I Year)"
    },
    "Civiligence": {
        "faculty": "Mr. Prateek Sharma",
        "students": "Aryan (I Year)"
    },
    "Synergy Greenscape": {
        "faculty": "Mr. Sonu Kumar",
        "students": "Shanvi (I Year)"
    },
    "TechnoScript": {
        "faculty": "Dr. Mayank Gupta & Dr. Shilpi Jain",
        "students": "Mukesh (II Year)"
    }
}

# Regex to strip phone numbers like [+91-9983800124] or (9983800124) or just 9571554444
# User wants to keep faculty numbers if they exist? No, user said "keep mobile number for faculty coordinator".
# This means I should not strip them if they are after a faculty name.

def strip_student_numbers(text):
    # This is complex because we need to know who is a student.
    # Usually students are listed after "Student Coordinator(s):"
    return text # Placeholder

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Find the coordinator sections and update them
    # For individual pages (Hero details and Footer):
    
    # 1. Update Hero Details Coordinator (if specific to event)
    # Example: Dr. Parveen Kumar [+91-7018106242]
    # We'll just manually target the specific names since the context is small
    
    # 2. Update Footer Support & Assistance (Global Replacements)
    # Student Coordinator: Harshit Garg [+91-9983800124] ... -> Harshit Garg
    # Faculty (Co-Convener/Convener): Keep
    
    # Let's target the exact list provided by user.
    
    # Compressive Edge Fix:
    if "Compressive Edge" in html or "ENGGCANVA" in html:
        html = html.replace("ENGGCANVA", "Compressive Edge")
        html = html.replace("Engineering Beyond Paper", "Cube Strength Challenge")
    
    # Manual Replacements for individual hero details:
    hero_replacements = [
        ("Dr. Parveen Kumar [+91-7018106242]", "Ar. Garima Kotnala"), # ArchiNova/Enggcanva catch
        ("Dr. Vishal Singhal [+91-9414779232]", "Mr. Prateek Sharma"), # Civiligence catch
    ]
    for old, new in hero_replacements:
        html = html.replace(old, new)

    # General strip student numbers from whole file
    # Pattern: [Name] 📞 [+91-XXXXXXXXXX] or just 📞 [+91-XXXXXXXXXX]
    # We only want to strip it if it's for Students.
    
    # In the footer:
    # <strong>Student Coordinator</strong>
    # <p style="font-size: 0.95rem;">Harshit Garg 📞 +91-9983800124</p>
    
    # We'll strip numbers from lines containing "Student Coordinator" or within that block
    student_section_regex = r'(<strong>Student Coordinator</strong>\s*<p[^>]*>)([^<]+)(📞\s*[\+\d -]+)(</p>)'
    html = re.sub(student_section_regex, r'\1\2\4', html, flags=re.MULTILINE)
    
    # Mobile menu/Dropdowns strip:
    # Student Coordinator: Mukesh (II Year) [+91-...]
    html = re.sub(r'(Student Coordinator:\s*[^<\r\n]+?)\s*\[\+91-[\d -]+\]', r'\1', html)
    html = re.sub(r'(Student Coordinator:\s*[^<\r\n]+?)\s*📞\s*[\+\d -]+', r'\1', html)

    # Update individual event pages' hero details with the new list
    # I'll do this by matching the file title or h1
    if "VisionVerse" in html or "Vision Verse" in html:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Dr. Ayush Meena<br>Student Coordinators: Aditya Alaria & Aryan\3', html, flags=re.DOTALL)
    elif "ProtoExpo" in html:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Mr. Mohit Kumar Tiwari<br>Student Coordinator: Santoshi Prajapat\3', html, flags=re.DOTALL)
    elif "ArchiNova" in html:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Ar. Garima Kotnala\3', html, flags=re.DOTALL)
    elif "ConcreTech" in html or "CreteCraft" in html:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Mr. Prateek Sharma<br>Student Coordinators: Minakshi Nathawat & Gargi Sharma\3', html, flags=re.DOTALL)
    elif "StructoBrick" in html:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Dr. Vishal Singhal<br>Student Coordinators: Rahul Kumar (I Year), Aryan (I Year)\3', html, flags=re.DOTALL)
    elif "Civiligence" in html:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Mr. Prateek Sharma<br>Student Coordinator: Aryan (I Year)\3', html, flags=re.DOTALL)
    elif "synergy-greenscape" in filepath:
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Mr. Sonu Kumar<br>Student Coordinator: Shanvi (I Year)\3', html, flags=re.DOTALL)
    elif "TechnoScript" in html:
        # TechnoScript details might be in a different div or the hero
        html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinators: Dr. Mayank Gupta & Dr. Shilpi Jain<br>Student Coordinator: Mukesh (II Year)\3', html, flags=re.DOTALL)
    elif "Bhavishya" in html:
         html = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1Faculty Coordinator: Dr. Santanu Malik<br>Student Coordinators: Harshit Garg & Priyanshu Raj\3', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

# Special Case: SkillForge.html needs both workshops listed
sf_path = os.path.join(base_dir, 'SkillForge.html')
if os.path.exists(sf_path):
    with open(sf_path, 'r', encoding='utf-8') as f:
        sf = f.read()
    new_details = '''For enquiries &amp; assistance:<br><br>
    <strong>Non-Destructive Testing (NDT):</strong><br>
    Faculty Coordinator: Dr. Santanu Malik<br>
    Student Coordinator: Shanvi (I Year)<br><br>
    <strong>Smart Construction using BIM:</strong><br>
    Faculty Coordinators: Dr. Ayush Meena, Mr. Mohit Kumar Tiwari, and Dr. Siddharth<br>
    Student Coordinators: Yashashvi, Vanshika Shrimal, &amp; Param'''
    sf = re.sub(r'(For enquiries &amp; assistance:<br><br>\s*)(.*?)(</div>)', r'\1' + new_details + r'\3', sf, flags=re.DOTALL)
    with open(sf_path, 'w', encoding='utf-8') as f:
        f.write(sf)

print("Coordinators updated.")
