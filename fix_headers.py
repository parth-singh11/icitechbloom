import os
import glob
import re

base_dir = r'c:\Users\Admin\OneDrive\Desktop\technew\ICI Techbloom'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

# Exclude index.html from hero styling since its hero is likely different (main landing)
# But we should check it. For now, focus on event sub-pages.
exclude_files = ['index.html', 'Events.html', 'glimpse.html']

for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in exclude_files:
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Standardize Header Styles in CSS
    # We want to find patterns like .xxx-hero h1 and .xxx-hero-subtitle
    # And replace font-size and add text-transform: uppercase;
    
    # regex for h1 font-size in hero
    # This might be tricky if they use different class names.
    # Let's try to find anything ending in -hero h1 or -hero-content h1
    
    css_patterns = [
        (r'(\.-hero\s*h1\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(2.4rem, 6vw, 4.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.archinova-hero\s*h1\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(2.4rem, 6vw, 4.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.engg-hero\s*h1\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(2.4rem, 6vw, 4.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.cc-hero\s*h1\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(2.4rem, 6vw, 4.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.civ-hero\s*h1\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(2.4rem, 6vw, 4.5rem)\3\n      text-transform: uppercase;'),
        
        # Subtitles
        (r'(\.-hero-subtitle\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(1.4rem, 3.5vw, 2.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.archinova-hero-subtitle\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(1.4rem, 3.5vw, 2.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.engg-hero-subtitle\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(1.4rem, 3.5vw, 2.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.cc-hero-subtitle\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(1.4rem, 3.5vw, 2.5rem)\3\n      text-transform: uppercase;'),
        (r'(\.civ-hero-subtitle\s*\{[^}]*font-size:\s*)([^;]+)(;)', r'\1clamp(1.4rem, 3.5vw, 2.5rem)\3\n      text-transform: uppercase;'),
    ]

    for pattern, repl in css_patterns:
        content = re.sub(pattern, repl, content, flags=re.IGNORECASE)

    # Ensure backdrop-filter and border are consistent in common hero boxes
    # Civiligence had: border: 3px solid var(--teal-dark); padding: 50px 40px; background: rgba(255,255,255,0.7); backdrop-filter: blur(3px);
    # Others might have color: #fff or background: rgba(0,0,0,0.1)
    
    # We will only apply these to the classes we know are "too large" or "messed up" - e.g. synergy-greenscape
    if filename in ['synergy-greenscape.html', 'ball-smash.html', 'SkillForge.html']:
         content = re.sub(r'(\.archinova-hero-content\s*\{[^}]*padding:\s*)([^;]+)(;)', r'\1 50px 40px\3', content)
         content = re.sub(r'(\.archinova-hero-content\s*\{[^}]*border:\s*)([^;]+)(;)', r'\1 3px solid var(--teal-dark)\3', content)
    
    # Manual catch-all for uppercase on h1 and subtitle even if font-size matched differently
    # content = re.sub(r'(<div class="[^"]*hero-subtitle">)(.*?)(</div>)', lambda m: m.group(1) + m.group(2).upper() + m.group(3), content)
    # Actually, CSS text-transform: uppercase is better.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Headers standardized.")
