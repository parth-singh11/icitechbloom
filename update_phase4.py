import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'

# 1. Update Timeline Table in index.html
index_file = os.path.join(base_dir, 'index.html')
with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Day 1 Table Body
day1_start_re = r'<tbody>\s*<tr>\s*<td style="text-align: center; vertical-align: middle;">08:00 AM to 09:00 AM</td>'
day1_end_re = r'<tr style="background:#da9694;">\s*<td colspan="2".*?>Day 1 End.*?</td>\s*</tr>\s*</tbody>'
day1_match = re.search(day1_start_re + r'.*?' + day1_end_re, content, flags=re.DOTALL)

if day1_match:
    new_day1 = '''<tbody>
              <tr>
                <td style="text-align: center; vertical-align: middle;">08:00 AM to 09:00 AM</td>
                <td style="vertical-align: middle;">Registration, kit distribution and Model Exhibition setup</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">09:00 AM to 10:30 AM</td>
                <td style="vertical-align: middle;">TechnoScript (TSCEI 2026) – Conference Sessions (Day 1) AND Civiligence (Day 1 – Screening Round)</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">10:30 AM to 11:00 AM</td>
                <td style="vertical-align: middle;">Welcome of Guests &amp; Inauguration</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">11:00 AM to 11:30 AM</td>
                <td style="vertical-align: middle;">High Tea</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">11:30 AM to 02:30 PM</td>
                <td style="vertical-align: middle;">ProtoExpo – Model Exhibition (Review)</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">08:00 AM to 02:30 PM</td>
                <td style="vertical-align: middle;">Vision Verse – Industry Expo</td>
              </tr>
              <tr style="background:#da9694;">
                <td colspan="2" style="text-align: center; font-weight: bold; color: #000; padding: 6px 16px;">Day 1 End
                </td>
              </tr>
            </tbody>'''
    content = content[:day1_match.start()] + new_day1 + content[day1_match.end():]

# Replace Day 2 Table Body
day2_start_re = r'<tbody>\s*<tr>\s*<td style="text-align: center; vertical-align: middle;">08:30 AM to 10:30 AM</td>'
day2_end_re = r'<tr style="background:#da9694;">\s*<td colspan="3".*?>Day 2 End.*?</td>\s*</tr>\s*</tbody>'
day2_match = re.search(day2_start_re + r'.*?' + day2_end_re, content, flags=re.DOTALL)

if day2_match:
    new_day2 = '''<tbody>
              <tr>
                <td style="text-align: center; vertical-align: middle;">08:30 AM to 10:30 AM</td>
                <td colspan="2" style="vertical-align: middle;">TechnoScript (TSCEI 2026) Sessions (Day 2) AND SkillForge Workshops (NDT &amp; BIM)</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">10:30 AM to 11:30 AM</td>
                <td colspan="2" style="vertical-align: middle;">ThinkTide – Expert Talks</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">11:30 AM to 01:30 PM</td>
                <td colspan="2" style="vertical-align: middle;">Engineer's Arena Competitions (ArchiNova, ConcreTech, StructoBrick, Civiligence Final)</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">11:30 AM to 01:30 PM</td>
                <td colspan="2" style="vertical-align: middle;">Synergy Greenscape (Poster display) AND Fun Activity</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">02:00 PM to 02:30 PM</td>
                <td colspan="2" style="vertical-align: middle;">Valedictory Ceremony and Prize Distribution</td>
              </tr>
              <tr style="background:#da9694;">
                <td colspan="3" style="text-align: center; font-weight: bold; color: #000; padding: 6px 16px;">Day 2 End
                </td>
              </tr>
            </tbody>'''
    content = content[:day2_match.start()] + new_day2 + content[day2_match.end():]

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Add Food Coupon Note globally to Fee Tables
html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Search for ending of the Registration Fees Table
    # The reg fees table often ends with Synergy Greenscape or similar.
    # We can just look for the end of the <tbody> for the table that has "Fee" in it or "ICI Member".
    # Since I don't know exactly, I'll inject a note BEFORE the Bank Details table or after the Fee table.
    
    # Actually, the user says: "Add a new row at the bottom of the table or a clear note beneath it stating: 'Optional: Food Coupon ₹150/head/Day (if required)'."
    # Let's add it as a new row in the fee table.
    # Find `Synergy Greenscape – Poster display` row and insert after it.
    syn_row_target = r'(<td>Synergy Greenscape – Poster display</td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>)'
    syn_row_add = r'\1\n        <tr>\n          <td colspan="3" style="text-align:center; font-weight:600; color:#1e4d3f; background:#f4f9f7;">Optional: Food Coupon ₹150/head/Day (if required)</td>\n        </tr>'
    new_html = re.sub(syn_row_target, syn_row_add, html, flags=re.DOTALL)
    
    # 3. Inject Fun Activity Banner in Events.html
    if 'Events.html' in filepath:
        # Find the end of `event-group` for `ev-arena`
        # Using string replacement
        target_inject = '''    </div>
  </div>

  <!-- ═══ REGISTRATION FEE TABLE ═══ -->'''
        
        fun_activity_html = '''    </div>
  </div>

  <div class="event-banner ev-funactivity" style="height:auto; min-height:160px; margin-bottom: 30px; display: flex; align-items: stretch; position: relative;">
    <div class="event-banner-bg" style="background:var(--teal-light); position:absolute; inset:0; opacity:0.9;"></div>
    <div class="event-banner-content" style="position:relative; z-index:2; flex-direction:column; align-items:flex-start; gap:8px; padding:20px 24px;">
      <span class="event-banner-title" style="color:#fff;">Fun Activity Section: Ball Smash - Wall Breaker Challenge</span>
      <span class="event-banner-subtitle" style="white-space:normal; line-height:1.4; color:rgba(255,255,255,0.9); font-size:1rem;">A purely fun, individual engagement activity where participants attempt to cause maximum destruction to a brick wall using a provided concrete ball. Designed for enjoyment to experience the thrill of demolition safely. No fee, open to all, no official winner declared.</span>
    </div>
  </div>

  <!-- ═══ REGISTRATION FEE TABLE ═══ -->'''
        new_html = new_html.replace(target_inject, fun_activity_html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Finished Timeline and Fee updates")
