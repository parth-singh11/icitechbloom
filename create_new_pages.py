import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
archinova_path = os.path.join(base_dir, 'ArchiNova  Designing Tomorrow.html')

with open(archinova_path, 'r', encoding='utf-8', errors='ignore') as f:
    template = f.read()

def create_page(filename, title, meta_desc, hero_title, hero_subtitle, start_time, end_time, venue, contact_name, contact_phone, content_html, register_btn=True):
    page = re.sub(r'<title>.*?</title>', f'<title>{title} — ICI TechBloom</title>', template)
    page = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta_desc}">', page)
    
    # Replace Hero Content
    hero_pattern = r'<div class="archinova-hero-content">.*?</div>\s*</section>'
    new_hero = f'''<div class="archinova-hero-content">
      <h1>{hero_title}</h1>
      <div class="archinova-hero-subtitle">{hero_subtitle}</div>
      <div class="archinova-hero-details">
        Time: {start_time} to {end_time}<br><br>
        Venue: {venue}<br><br>
        For enquiries &amp; assistance:<br><br>
        {contact_name} [{contact_phone}]
      </div>
    </div>
  </section>'''
    page = re.sub(hero_pattern, new_hero, page, flags=re.DOTALL)
    
    # Replace the body sections (Overview, Guidelines, Evaluation) with empty, then insert our content_html
    body_pattern = r'<!-- ═══ OVERVIEW ═══ -->.*?<!-- ═══ ACTION BUTTONS ═══ -->'
    page = re.sub(body_pattern, content_html + '\n  <!-- ═══ ACTION BUTTONS ═══ -->', page, flags=re.DOTALL)
    
    if not register_btn:
        page = page.replace('<a href="Events.html" class="register-btn-header">Register Now</a>', '')
        
    with open(os.path.join(base_dir, filename), 'w', encoding='utf-8') as f:
        f.write(page)

# Synergy Greenscape Content
synergy_content = '''
  <!-- ═══ OVERVIEW ═══ -->
  <div class="section-teal-header">Overview</div>
  <section class="cc-section">
    <div class="cc-content">
      <h2 class="teal-heading-large">Synergy Greenscape – Poster Display</h2>
      
      <p>Synergy Greenscape is a multidisciplinary poster display and evaluation event that invites students from all academic backgrounds to collectively reimagine a Green Campus. The event emphasizes how collaboration among engineering, science, management, humanities, commerce, health, and law can transform a conventional educational campus into a sustainable, smart, inclusive, and future-ready ecosystem.</p>
      <p style="margin-top:12px;">Participants will design posters prior to the event and display them on the event day for expert evaluation. The focus is on practical, implementable ideas that promote environmental responsibility, resource efficiency, and social well-being within campuses.</p>

      <h3 class="archinova-heading">Event Theme</h3>
      <p style="font-weight:600; font-style:italic;">"Green Campus: Where Every Discipline Shapes a Sustainable Future"</p>
      <p>The theme highlights that sustainability is not limited to one branch, but is a shared responsibility where technical innovation, policy, economics, creativity, and social awareness work together.</p>

      <h3 class="archinova-heading">Objective of the Event</h3>
      <ul class="cc-list">
        <li>To promote sustainability-oriented thinking among students of all disciplines.</li>
        <li>To encourage interdisciplinary collaboration for campus-level solutions.</li>
        <li>To showcase practical and innovative ideas for green, smart, and healthy campuses.</li>
        <li>To create awareness about environmental responsibility through visual communication.</li>
      </ul>
    </div>
  </section>

  <!-- ═══ TASK & GUIDELINES ═══ -->
  <div class="section-teal-header">Task Description &amp; Guidelines</div>
  <section class="cc-section">
    <div class="cc-content">
      <h3 class="archinova-heading">Task Description</h3>
      <p>Participants are required to design a poster in advance based on the Green Campus concept. On the day of the event, participants will display their posters at the allotted venue, explain their ideas to the judges, and respond to questions. The poster must present multidisciplinary solutions for creating a sustainable educational campus, addressing:</p>
      <ul class="cc-list">
        <li>Energy conservation</li>
        <li>Water management</li>
        <li>Waste reduction and recycling</li>
        <li>Health, hygiene, and well-being</li>
        <li>Environmental awareness</li>
        <li>Innovation and smart campus development</li>
      </ul>

      <h3 class="archinova-heading">Multidisciplinary Contribution Framework</h3>
      <p>Posters should clearly highlight how students from different fields can contribute:</p>
      <ul class="cc-list">
        <li><strong>Engineering &amp; Technology</strong> - Renewable energy, green buildings, smart infrastructure</li>
        <li><strong>Science</strong> - Environmental research, biodiversity conservation, pollution control</li>
        <li><strong>Management</strong> - Resource planning, sustainability policies, green finance</li>
        <li><strong>Arts &amp; Humanities</strong> - Awareness campaigns, behavioral change, creative outreach</li>
        <li><strong>Commerce &amp; Economics</strong> - Cost-benefit analysis, green entrepreneurship</li>
        <li><strong>Health &amp; Social Sciences</strong> - Hygiene, mental well-being, community impact</li>
        <li><strong>Law &amp; Governance</strong> - Environmental regulations, campus sustainability policies</li>
      </ul>

      <h3 class="archinova-heading">Poster Specifications</h3>
      <ul class="cc-list">
        <li><strong>Topic:</strong> Green Campus Concept</li>
        <li><strong>Poster Size:</strong> A1</li>
        <li><strong>Orientation:</strong> Portrait or Landscape</li>
        <li><strong>Poster must include:</strong> 1. Introduction, 2. Components of a Green Campus, 3. Role of All Branches, 4. Implementation Plan, 5. Benefits and Conclusion.</li>
        <li><strong>Visuals:</strong> Diagrams, charts, flowcharts, and illustrations are strongly encouraged.</li>
      </ul>

      <h3 class="archinova-heading">Guidelines &amp; Rules</h3>
      <ul class="cc-list">
        <li>Teams may consist of 1 participant only.</li>
        <li>Posters must be prepared by participants prior to the event.</li>
        <li>Only display and explanation will take place on the event day.</li>
        <li>Content must be original and theme-oriented. Plagiarism is strictly prohibited.</li>
      </ul>
    </div>
  </section>

  <!-- ═══ EVALUATION ═══ -->
  <div class="section-teal-header">Evaluation and Disqualification Criteria</div>
  <section class="cc-section">
    <div class="cc-content">
      <h3 class="archinova-heading">Evaluation Criteria</h3>
      <table class="custom-table" style="margin-top:16px;">
        <thead>
          <tr style="background:#1e4d3f; color:#fff;">
            <th>Criteria</th>
            <th>Marks</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Content &amp; Technical Depth</td><td>30 Marks</td></tr>
          <tr><td>Creativity &amp; Visual Appeal</td><td>25 Marks</td></tr>
          <tr><td>Practical Implementation Ideas</td><td>20 Marks</td></tr>
          <tr><td>Presentation &amp; Explanation</td><td>15 Marks</td></tr>
          <tr><td>Response to Questions</td><td>10 Marks</td></tr>
          <tr style="font-weight:bold; background:#f4f9f7;"><td>Total</td><td>100 Marks</td></tr>
        </tbody>
      </table>

      <h3 class="archinova-heading" style="margin-top:30px;">Disqualification Criteria</h3>
      <ul class="cc-list">
        <li>Use of plagiarized or copied content.</li>
        <li>Late arrival after the briefing.</li>
        <li>Misbehavior during the event or disturbing other participants.</li>
      </ul>
    </div>
  </section>
'''

create_page('synergy-greenscape.html', 'Synergy Greenscape', 'Synergy Greenscape - Poster Display at ICI TechBloom 26', 'Synergy Greenscape', 'Designing Sustainable Campuses Through Multidisciplinary Innovation', '11:30 AM', '01:30 PM', 'Exhibition Area', 'Event Coordinator', '+91-XXXXXXXXXX', synergy_content)

# Ball Smash Content
ball_smash_content = '''
  <!-- ═══ OVERVIEW ═══ -->
  <div class="section-teal-header">Overview</div>
  <section class="cc-section">
    <div class="cc-content">
      <h2 class="teal-heading-large">Concrete Ball Smash – Wall Breaker Challenge</h2>
      
      <p>The event aims to create an entertaining and interactive experience for participants while introducing a basic understanding of impact and structural behavior in a playful manner. The activity encourages enthusiasm, teamwork, and healthy competition among students.</p>

      <h3 class="archinova-heading">Event Description</h3>
      <p>"Concrete Ball Smash Wall Breaker Challenge" is a fun-based event in which participants attempt to break a brick wall using a concrete ball provided by the organizers. The objective is to cause the maximum number of bricks to fall through effective impact. The event is designed purely for enjoyment and engagement, allowing participants to experience the thrill of demolition in a safe and controlled environment.</p>

      <h3 class="archinova-heading">Participation Details</h3>
      <ul class="cc-list">
        <li><strong>Team Size:</strong> Individual</li>
        <li>Open for all branches and years</li>
        <li>No fee, open to all, no official winner declared.</li>
      </ul>
    </div>
  </section>

  <!-- ═══ GUIDELINES ═══ -->
  <div class="section-teal-header">Procedure &amp; Rules</div>
  <section class="cc-section">
    <div class="cc-content">
      <h3 class="archinova-heading">Event Procedure</h3>
      <ul class="cc-list">
        <li>A brick wall will be arranged by the event team as per predefined dimensions.</li>
        <li>The concrete ball will be provided by the organizers to ensure uniformity for all participants.</li>
        <li>Each participant/team will be given a fixed number of attempts to strike the wall.</li>
        <li>After each strike, the number of bricks fallen will be counted.</li>
        <li>The participant/team causing the highest number of bricks to fall will be declared the winner.</li>
      </ul>
      <p style="font-weight:600; color:#d9534f; margin-top:12px;">Note: The activity is conducted only for fun participation; no official winner or prize will be declared.</p>

      <h3 class="archinova-heading" style="margin-top:24px;">Judging Criteria</h3>
      <ul class="cc-list">
        <li>Maximum number of bricks fallen</li>
        <li>Effectiveness of impact</li>
        <li>Adherence to event rules</li>
      </ul>

      <h3 class="archinova-heading" style="margin-top:24px;">Safety Measures</h3>
      <ul class="cc-list">
        <li>A safe distance will be maintained between the striking zone and spectators.</li>
        <li>Only authorized volunteers will handle the concrete ball.</li>
        <li>Participants must follow instructions given by coordinators at all times.</li>
        <li>Protective barricading will be installed around the activity area.</li>
      </ul>
    </div>
  </section>
'''

create_page('ball-smash.html', 'Ball Smash - Wall Breaker Challenge', 'Fun Activity - Concrete Ball Smash at ICI TechBloom 26', 'Ball Smash', 'Wall Breaker Challenge', '11:30 AM', '01:30 PM', 'Activity Ground', 'Event Coordinator', '+91-XXXXXXXXXX', ball_smash_content, register_btn=False)

# Link new pages globally
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Append to dropdown
    tgt_desktop1 = '<a href="VisionVerse Industry Exhibition A Gallery of.html">VisionVerse</a>'
    if tgt_desktop1 in html and '<a href="synergy-greenscape.html">' not in html:
        html = html.replace(tgt_desktop1, tgt_desktop1 + '\n          <a href="synergy-greenscape.html">Synergy Greenscape</a>\n          <a href="ball-smash.html">Ball Smash</a>')

    tgt_mobile1 = '<a href="VisionVerse Industry Exhibition A Gallery of.html">&nbsp;&nbsp;— VisionVerse</a>'
    if tgt_mobile1 in html and '<a href="synergy-greenscape.html">&nbsp;&nbsp;— Synergy Greenscape</a>' not in html:
        html = html.replace(tgt_mobile1, tgt_mobile1 + '\n    <a href="synergy-greenscape.html">&nbsp;&nbsp;— Synergy Greenscape</a>\n    <a href="ball-smash.html">&nbsp;&nbsp;— Ball Smash</a>')

    if '\\Events.html' in filepath or '/Events.html' in filepath:
        # Link Synergy Greenscape in Engineer's Arena dropdown correctly
        html = html.replace('<a href="javascript:void(0);">\n          <span class="dropdown-item-title">Synergy Greenscape</span>', '<a href="synergy-greenscape.html">\n          <span class="dropdown-item-title">Synergy Greenscape</span>')
        
        # Exact replacement of Ball Smash div injected earlier to an <a> tag
        old_div = (
            '  <div class="event-banner ev-funactivity" style="height:auto; min-height:160px; margin-bottom: 30px; display: flex; align-items: stretch; position: relative;">\\n'
            '    <div class="event-banner-bg" style="background:var(--teal-light); position:absolute; inset:0; opacity:0.9;"></div>\\n'
            '    <div class="event-banner-content" style="position:relative; z-index:2; flex-direction:column; align-items:flex-start; gap:8px; padding:20px 24px;">\\n'
            '      <span class="event-banner-title" style="color:#fff;">Fun Activity Section: Ball Smash - Wall Breaker Challenge</span>\\n'
            '      <span class="event-banner-subtitle" style="white-space:normal; line-height:1.4; color:rgba(255,255,255,0.9); font-size:1rem;">A purely fun, individual engagement activity where participants attempt to cause maximum destruction to a brick wall using a provided concrete ball. Designed for enjoyment to experience the thrill of demolition safely. No fee, open to all, no official winner declared.</span>\\n'
            '    </div>\\n'
            '  </div>'
        )
  
        new_a = (
            '  <a href="ball-smash.html" class="event-banner ev-funactivity" style="height:auto; min-height:160px; margin-bottom: 30px; display: flex; align-items: stretch; position: relative; text-decoration:none;">\\n'
            '    <div class="event-banner-bg" style="background:var(--teal-light); position:absolute; inset:0; opacity:0.9;"></div>\\n'
            '    <div class="event-banner-content" style="position:relative; z-index:2; flex-direction:column; align-items:flex-start; gap:8px; padding:20px 24px;">\\n'
            '      <span class="event-banner-title" style="color:#fff;">Ball Smash - Wall Breaker Challenge</span>\\n'
            '      <span class="event-banner-subtitle" style="white-space:normal; line-height:1.4; color:rgba(255,255,255,0.9); font-size:1rem;">A purely fun, individual engagement activity where participants attempt to cause maximum destruction to a brick wall using a provided concrete ball. Designed for enjoyment to experience the thrill of demolition safely. No fee, open to all, no official winner declared.</span>\\n'
            '    </div>\\n'
            '  </a>'
        )
        html = html.replace(old_div, new_a)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Created new pages and linked them globally")
