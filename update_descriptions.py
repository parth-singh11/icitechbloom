import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

def replace_in_file(filepath, tgt, repl):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    content = content.replace(tgt, repl)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # ArchiNova Dropdown Description
    tgt_ar = '<span class="dropdown-item-desc">Exterior Wall Elevation Challenge using slim tiles (2 Hours, Software-based design of an 8m x 13m elevation).</span>'
    repl_ar = '<span class="dropdown-item-desc">Exterior Wall Elevation Challenge using Slim tiles. Target: Interior Design Students. 2 Hours, Software-based design of an 8m x 13m elevation. Evaluation based on Creativity, Material Expression, and Architectural Identity.</span>'
    content = content.replace(tgt_ar, repl_ar)

    tgt_ar2 = '<span class="dropdown-item-desc">Designing Tomorrow</span>'
    content = content.replace(tgt_ar2, repl_ar)

    # ConcreTech Dropdown Description
    tgt_co = '<span class="dropdown-item-desc">High-Performance Concrete Mix Design and Slump Test evaluation.</span>'
    repl_co = '<span class="dropdown-item-desc">High-Performance Concrete Mix Design. Focuses on preparing a concrete mix and demonstrating precision in the standard slump test within 20 minutes.</span>'
    content = content.replace(tgt_co, repl_co)

    tgt_co2 = '<span class="dropdown-item-desc">Strength in Every Mix</span>'
    content = content.replace(tgt_co2, repl_co)

    # StructoBrick Dropdown Description
    tgt_st = '<span class="dropdown-item-desc">Stepped Brick Wall Construction (Max height: 4 bricks).</span>'
    repl_st = '<span class="dropdown-item-desc">Brick Construction Skills Challenge. Construct a stepped brick wall (without plastering) up to a max height of 4 bricks.</span>'
    content = content.replace(tgt_st, repl_st)

    tgt_st2 = '<span class="dropdown-item-desc">Rise One Block at a Time</span>'
    content = content.replace(tgt_st2, repl_st)

    # Civiligence Dropdown Description
    tgt_ci = '<span class="dropdown-item-desc">Day 1: Online Screening Quiz. Day 2: On-stage Final Quiz.</span>'
    repl_ci = '<span class="dropdown-item-desc">Day 1: Online Screening Quiz (30 MCQs, top 5 qualify). Day 2: Offline On-Stage Final Quiz featuring Rapid Fire, Written, and Visual rounds.</span>'
    content = content.replace(tgt_ci, repl_ci)

    tgt_ci2 = '<span class="dropdown-item-desc">Technical Quiz</span>'
    content = content.replace(tgt_ci2, repl_ci)

    # Update Synergy Greenscape explicitly
    tgt_syn = '<span class="dropdown-item-desc">Poster display</span>'
    repl_syn = '<span class="dropdown-item-desc">A multidisciplinary poster display inviting students to reimagine a Green Campus. Participants design A1 posters prior to the event focusing on energy, water, waste, and health, demonstrating how different engineering and non-engineering branches contribute to sustainability. Evaluated on Content, Creativity, and Practical Implementation.</span>'
    content = content.replace(tgt_syn, repl_syn)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Finished Dropdown Updates")
