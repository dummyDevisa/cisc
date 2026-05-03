import re

with open('dashboards_mockups.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce panel padding
content = re.sub(r'padding:\s*15px;', 'padding: 10px 15px;', content)

# 2. Reduce header margin (mb-3 -> mb-1)
# Note: we need to be careful to target the headers of the 4 panels
content = re.sub(r'<div class="flex justify-between items-center mb-3">', r'<div class="flex justify-between items-center mb-1">', content)

# 3. Reduce KPI grid margin (mb-4 -> mb-1)
content = re.sub(r'<div class="grid grid-cols-4 gap-2 mb-4">', r'<div class="grid grid-cols-4 gap-2 mb-1">', content)
content = re.sub(r'<div class="grid grid-cols-2 gap-2 mb-4">', r'<div class="grid grid-cols-2 gap-2 mb-1">', content)

# 4. Reduce Footer margins (mt-4 pt-3 -> mt-1 pt-1)
content = re.sub(r'class="mt-4 grid grid-cols-2 gap-4 border-t pt-3"', r'class="mt-1 grid grid-cols-2 gap-4 border-t pt-1"', content)

# 5. Fix typo in background class if exists
content = re.sub(r'bg-slate-800/50/50', 'bg-slate-800/50', content)

# 6. Reduce data value font size slightly in KPIs inside the panels to save vertical space if needed (optional, keeping it for now but reducing padding)
content = re.sub(r'p-2 rounded border border-slate-700', 'px-2 py-1 rounded border border-slate-700', content)

# 7. Modify the .data-panel flex header padding in CSS
content = re.sub(r'padding-bottom: 8px;', 'padding-bottom: 2px;', content)
content = re.sub(r'margin-bottom: 12px;', 'margin-bottom: 4px;', content)

with open('dashboards_mockups.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Panel internal spacing compressed.")
