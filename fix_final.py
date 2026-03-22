import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'

# 1. Update Navigation Links
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # In Desktop Nav Dropdown:
    # Original:
    # <a href="javascript:void(0);">Non-Destructive Testing (NDT) of Structures</a>
    # <a href="javascript:void(0);">Smart Construction using BIM</a>
    
    desktop_regex = r'<a href="javascript:void\(0\);">Non-Destructive Testing \(NDT\) of Structures</a>\s*<a href="javascript:void\(0\);">Smart Construction using BIM</a>'
    html = re.sub(desktop_regex, '<a href="SkillForge.html">SkillForge Series Workshop</a>', html)

    # In Mobile Menu:
    mobile_regex = r'<a href="javascript:void\(0\);">&nbsp;&nbsp;— NDT of Structures</a>\s*<a href="ProtoExpo Showcasing Ideas in Action.html">'
    html = re.sub(mobile_regex, r'<a href="SkillForge.html">&nbsp;&nbsp;— SkillForge</a>\n    <a href="ProtoExpo Showcasing Ideas in Action.html">', html)

    # Note: Some references to 'Smart Construction' might have been lost or wrapped differently in the mobile menu
    # Let's brute force removal of mobile NDT if the regex failed.
    html = html.replace('<a href="javascript:void(0);">&nbsp;&nbsp;— NDT of Structures</a>', '<a href="SkillForge.html">&nbsp;&nbsp;— SkillForge</a>')
    html = html.replace('<a href="javascript:void(0);">&nbsp;&nbsp;— Smart Construction using BIM</a>\n', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Fix Ball Smash action buttons
ball_smash_path = os.path.join(base_dir, 'ball-smash.html')
if os.path.exists(ball_smash_path):
    with open(ball_smash_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove action buttons chunk entirely
    html = re.sub(r'<!-- ═══ ACTION BUTTONS ═══ -->.*?<!-- ═══ FOOTER ═══ -->', '<!-- ═══ FOOTER ═══ -->', html, flags=re.DOTALL)
    
    # Wrap table safely if any, but Ball Smash doesn't have a table. Just list.
    with open(ball_smash_path, 'w', encoding='utf-8') as f:
        f.write(html)

# 3. Create SkillForge.html
archinova_path = os.path.join(base_dir, 'ArchiNova  Designing Tomorrow.html')
with open(archinova_path, 'r', encoding='utf-8', errors='ignore') as f:
    template = f.read()

skillforge_content = '''
  <!-- ═══ OVERVIEW ═══ -->
  <div class="section-teal-header">SkillForge Series Workshop</div>
  <section class="cc-section">
    <div class="cc-content">
      <p>The SkillForge Series embodies practical mind-on sessions crafted to shape your tomorrow. These interactive workshops introduce foundational and cutting-edge engineering skills directly required by modern industry practices.</p>

      <h3 class="archinova-heading" style="color:var(--teal); font-size:1.4rem; border-bottom:1px solid #ddd; padding-bottom:8px; margin-top:40px;">Workshop 1: Non-Destructive Testing (NDT) of Structures</h3>
      <p>This hands-on workshop dives into the methodologies and equipment used to evaluate the properties of a material, component, or system without causing damage. Essential for maintaining the integrity and safety of structures, NDT techniques taught will bridge the gap between academic theory and field applications.</p>
      
      <h3 class="archinova-heading" style="color:var(--teal); font-size:1.4rem; border-bottom:1px solid #ddd; padding-bottom:8px; margin-top:40px;">Workshop 2: Smart Construction using BIM</h3>
      <p>Building Information Modeling (BIM) is revolutionizing the construction industry globally. This workshop covers the transformation of digital representations into physical and functional structures. Learn how BIM empowers architects, engineers, and construction professionals to plan, design, and manage infrastructure seamlessly.</p>
      
      <p style="margin-top:40px; font-weight:600; font-size:1.1rem; color:#1e4d3f;">Eligibility:</p>
      <ul class="cc-list">
        <li>Open to all active engineering students.</li>
        <li>No registration fee applied for either workshop.</li>
      </ul>
    </div>
  </section>
'''

# Build SkillForge
page = re.sub(r'<title>.*?</title>', '<title>SkillForge Series Workshop — ICI TechBloom</title>', template)
page = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="SkillForge Series Workshop - NDT and BIM">', page)

hero_pattern = r'<div class="archinova-hero-content">.*?</div>\s*</section>'
new_hero = f'''<div class="archinova-hero-content">
  <h1>SkillForge Series Workshop</h1>
  <div class="archinova-hero-subtitle">Minds on sessions to shape your tomorrow</div>
  <div class="archinova-hero-details">
    Time: 08:30 AM to 10:30 AM<br><br>
    Venue: Assigned Lab Areas<br><br>
    For enquiries &amp; assistance:<br><br>
    SkillForge Coordinator [+91-XXXXXXXXXX]
  </div>
</div>
</section>'''
page = re.sub(hero_pattern, new_hero, page, flags=re.DOTALL)

body_pattern = r'<!-- ═══ OVERVIEW ═══ -->.*?<!-- ═══ ACTION BUTTONS ═══ -->'
page = re.sub(body_pattern, skillforge_content + '\\n  <!-- ═══ ACTION BUTTONS ═══ -->', page, flags=re.DOTALL)

# Delete "For Reference" action button leaving only "Register Now" if desired, or remove the action buttons fully since the workshops are No Fee according to tables. But wait! The event table says "No Fee". But they might need to register via google forms. I'll just remove "For Reference" button.
page = re.sub(r'<a href="#" class="archinova-btn">For Reference</a>\s*<div class="dashed-divider"></div>', '', page)

# Update the Event links inside Events.html to route ev-skillforge to SkillForge.html
events_file = os.path.join(base_dir, 'Events.html')
if os.path.exists(events_file):
    with open(events_file, 'r', encoding='utf-8') as f:
        ev_html = f.read()
    
    # ev-skillforge was set to toggle dropdown previously, let's just leave it or set href if it was an <a> tag
    # In earlier runs, we didn't touch the root `div` of ev-skillforge but it had `onclick="this.parentElement.classList.toggle('open')"`.
    # To fix formatting, let's keep it as is, or we change it to link directly to `SkillForge.html`.
    # I'll just change the dropdown children links, which I did in the global replacement above!
    pass

with open(os.path.join(base_dir, 'SkillForge.html'), 'w', encoding='utf-8') as f:
    f.write(page)

# To fix "formatting and styling is little messed up" on synergy greenscape:
# Remove "For Reference" button as well there.
syn_path = os.path.join(base_dir, 'synergy-greenscape.html')
if os.path.exists(syn_path):
    with open(syn_path, 'r', encoding='utf-8') as f:
        s_html = f.read()
    s_html = re.sub(r'<a href="#" class="archinova-btn">For Reference</a>\s*<div class="dashed-divider"></div>', '', s_html)
    with open(syn_path, 'w', encoding='utf-8') as f:
        f.write(s_html)

print("Finished fixing SkillForge integration")
