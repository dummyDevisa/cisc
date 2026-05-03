import re

with open('dashboards_mockups.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the status-row block
pattern = r'(<div class="status-row">.*?</div>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    status_row_block = match.group(1)
    # Remove it from its original position
    content = content.replace(status_row_block, '', 1)
    
    # Insert it inside map-section, before hud-overlay
    insertion_point = r'<main class="map-section">'
    replacement = f'<main class="map-section">\n        {status_row_block}'
    content = content.replace(insertion_point, replacement, 1)

with open('dashboards_mockups.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Status-row moved inside map-section.")
