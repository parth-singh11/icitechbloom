import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Update Navigation Links (Global)
    nav_workshop_target = '''<a href="CreteCraft Concrete Mix Design  Principles.html">CreteCraft</a>
          <a href="Protecting Research  Innovation through Patents.html">Protecting Research through Patents</a>'''
    nav_workshop_repl = '''<a href="javascript:void(0);">Non-Destructive Testing (NDT) of Structures</a>
          <a href="javascript:void(0);">Smart Construction using BIM</a>'''
    # Handle possible variations without the second link in case it was already removed
    content = content.replace(nav_workshop_target, nav_workshop_repl)

    # Alternate match for just CreteCraft in nav
    nav_cretecraft_target = '<a href="CreteCraft Concrete Mix Design  Principles.html">CreteCraft</a>'
    nav_cretecraft_repl = '<a href="javascript:void(0);">Non-Destructive Testing (NDT) of Structures</a>'
    content = content.replace(nav_cretecraft_target, nav_cretecraft_repl)
    
    nav_patents_target = '<a href="Protecting Research  Innovation through Patents.html">Protecting Research through Patents</a>'
    nav_patents_repl = '<a href="javascript:void(0);">Smart Construction using BIM</a>'
    content = content.replace(nav_patents_target, nav_patents_repl)

    # Update Mobile Nav Links
    mobile_cretecraft_target = '<a href="CreteCraft Concrete Mix Design  Principles.html">&nbsp;&nbsp;— CreteCraft</a>'
    mobile_cretecraft_repl = '<a href="javascript:void(0);">&nbsp;&nbsp;— NDT of Structures</a>'
    content = content.replace(mobile_cretecraft_target, mobile_cretecraft_repl)

    mobile_patents_target = '<a href="Protecting Research  Innovation through Patents.html">&nbsp;&nbsp;— Protecting Research through Patents</a>'
    mobile_patents_repl = '<a href="javascript:void(0);">&nbsp;&nbsp;— Smart Construction using BIM</a>'
    content = content.replace(mobile_patents_target, mobile_patents_repl)
    
    # 2. Update Timeline Table in index.html Day 2
    if 'index.html' in filepath:
        timeline_target = 'CreteCraft: Innovations in Concrete Mix Design and Applications</td>'
        timeline_repl = 'Non-Destructive Testing (NDT) of Structures</td>'
        content = content.replace(timeline_target, timeline_repl)
    
    # 3. Events.html SkillForge descriptions and Engineer's Arena descriptions
    if 'Events.html' in filepath:
        # SkillForge
        sf_target = '''<a href="CreteCraft Concrete Mix Design  Principles.html">
          <span class="dropdown-item-title">CreteCraft</span>
          <span class="dropdown-item-desc">Concrete Mix Design – Principles, Practices, and Applications of Different Types of Concrete</span>
        </a>
        <a href="Protecting Research  Innovation through Patents.html">
          <span class="dropdown-item-title">Protecting Research &amp; Innovation</span>
          <span class="dropdown-item-desc">through Patents and Industrial Designs</span>
        </a>'''
        sf_repl = '''<a href="javascript:void(0);">
          <span class="dropdown-item-title">Non-Destructive Testing (NDT) of Structures</span>
          <span class="dropdown-item-desc">Workshop on NDT practices and techniques</span>
        </a>
        <a href="javascript:void(0);">
          <span class="dropdown-item-title">Smart Construction using BIM</span>
          <span class="dropdown-item-desc">Workshop on Building Information Modeling applications</span>
        </a>'''
        content = content.replace(sf_target, sf_repl)
        
        # Engineer's Arena Descriptions
        ea_archinova = '<span class="dropdown-item-desc">Designing Tomorrow</span>'
        ea_archinova_repl = '<span class="dropdown-item-desc">Exterior Wall Elevation Challenge using slim tiles (2 Hours, Software-based design of an 8m x 13m elevation).</span>'
        content = content.replace(ea_archinova, ea_archinova_repl)
        
        ea_concretech = '<span class="dropdown-item-desc">Strength in Every Mix</span>'
        ea_concretech_repl = '<span class="dropdown-item-desc">High-Performance Concrete Mix Design and Slump Test evaluation.</span>'
        content = content.replace(ea_concretech, ea_concretech_repl)
        
        ea_structo = '<span class="dropdown-item-desc">Rise One Block at a Time</span>'
        ea_structo_repl = '<span class="dropdown-item-desc">Stepped Brick Wall Construction (Max height: 4 bricks).</span>'
        content = content.replace(ea_structo, ea_structo_repl)
        
        ea_civili = '<span class="dropdown-item-desc">Technical Quiz</span>'
        ea_civili_repl = '<span class="dropdown-item-desc">Day 1: Online Screening Quiz. Day 2: On-stage Final Quiz.</span>'
        content = content.replace(ea_civili, ea_civili_repl)

    # 4. Fee Tables (Remove Quizcrete & Enggcanva, Add Synergy Greenscape)
    # The structure looks like this:
    # <tr>
    #   <td>Quizcrete – Where Knowledge Meets Strength</td>
    #   <td>₹...</td>
    #   <td>₹...</td>
    # </tr>
    # Use re to remove them.
    content = re.sub(r'<tr>\s*<td>Quizcrete – .*?</td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>', '', content, flags=re.DOTALL)
    content = re.sub(r'<tr>\s*<td>Enggcanva – .*?</td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>', '', content, flags=re.DOTALL)
    
    # Add Synergy Greenscape if not present
    synergy_row = '''<tr>
          <td>Synergy Greenscape – Poster display</td>
          <td>₹100 (ICI Member)</td>
          <td>₹150 (Non-Member)</td>
        </tr>'''
    
    structobrick_target_re = r'(<tr>\s*<td>StructoBrick – .*?</td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>)'
    
    if "Synergy Greenscape – Poster display" not in content and "StructoBrick" in content:
        # Avoid matching non-fee table things, but Structobrick row is unique enough
        content = re.sub(structobrick_target_re, r'\1\n        ' + synergy_row, content, flags=re.DOTALL)

    # 5. TechnoScript tracks update
    # Instructions: "TechnoScript (Conference): Update the title to "TSCEI 2026". Update the descriptive tracks to focus on: Sustainable Civil Engineering, Smart Infrastructure & Digital Construction, Climate-Resilient Infrastructure, Water Resources, AI/IoT in Civil Engineering, and Interdisciplinary Solutions."
    if 'TechnoScript' in filepath or 'TSCEI' in filepath:
        # Find the Tracks header and replace the list
        # It probably has something like <ul class="conference-tracks"> or similar.
        pass # I will do this manually to be safe

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Executed comprehensive structural updates')
