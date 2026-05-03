import re

with open('dashboards_mockups.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace dark colors with vibrant variants for dark mode
content = re.sub(r'text-green-600', 'text-green-400', content)
content = re.sub(r'text-orange-600', 'text-orange-400', content)
content = re.sub(r'text-red-600', 'text-red-400', content)
content = re.sub(r'text-blue-600', 'text-blue-400', content)
content = re.sub(r'text-red-700', 'text-red-500', content)

# Fix specifically neighborhood names if they are still dark
content = re.sub(r'text-slate-800', 'text-white', content)
content = re.sub(r'text-slate-900', 'text-white', content)

with open('dashboards_mockups.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Text colors adjusted for dark mode contrast.")
