import re

with open('dashboards_mockups.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Variables
content = re.sub(r'--bg-light: #f8fafc;', '--bg-light: #0f172a;', content)
content = re.sub(r'--panel-bg: #ffffff;', '--panel-bg: #1e293b;', content)
content = re.sub(r'--border: #e2e8f0;', '--border: #334155;', content)
content = re.sub(r'--text-main: #0f172a;', '--text-main: #f1f5f9;', content)
content = re.sub(r'--text-dim: #64748b;', '--text-dim: #94a3b8;', content)

# Header & specific elements
content = re.sub(r'background: #ffffff;', 'background: var(--panel-bg);', content)
content = re.sub(r'border-bottom: 1px solid #e2e8f0;', 'border-bottom: 1px solid var(--border);', content)

# Tailwind classes for colors
content = re.sub(r'bg-white', 'bg-slate-800', content)
content = re.sub(r'bg-slate-50', 'bg-slate-800/50', content)
content = re.sub(r'border-slate-100', 'border-slate-700', content)
content = re.sub(r'text-slate-700', 'text-slate-300', content)
content = re.sub(r'text-slate-600', 'text-slate-400', content)
content = re.sub(r'text-slate-900', 'text-slate-100', content)
content = re.sub(r'bg-slate-200/50', 'bg-slate-700/50', content)

# Typography scaling
content = re.sub(r'text-\[8px\]', 'text-[11px]', content)
content = re.sub(r'text-\[9px\]', 'text-[12px]', content)
content = re.sub(r'text-\[10px\]', 'text-[13px]', content)
content = re.sub(r'text-\[11px\]', 'text-[14px]', content)
content = re.sub(r'text-\[12px\]', 'text-[15px]', content)

# Protocol box backgrounds
content = re.sub(r'bg-green-50\b', 'bg-green-900/20 text-green-300', content)
content = re.sub(r'bg-yellow-50\b', 'bg-yellow-900/20 text-yellow-300', content)
content = re.sub(r'bg-orange-50\b', 'bg-orange-900/20 text-orange-300', content)
content = re.sub(r'bg-red-50\b', 'bg-red-900/20 text-red-300', content)
content = re.sub(r'text-green-900', 'text-green-300', content)
content = re.sub(r'text-yellow-900', 'text-yellow-300', content)
content = re.sub(r'text-orange-900', 'text-orange-300', content)
content = re.sub(r'text-red-900', 'text-red-300', content)

# Map adjustments for dark mode
content = re.sub(
    r"L\.tileLayer\('https://{s}\.basemaps\.cartocdn\.com/light_all/{z}/{x}/{y}{r}\.png'",
    "L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'",
    content
)

# Map labels scaling
content = re.sub(r'font-size: 10px;', 'font-size: 12px;', content)
content = re.sub(r'font-size: 8px;', 'font-size: 11px;', content)

# Charts config
content = re.sub(r'height: 140', 'height: 180', content)
content = re.sub(r"theme: \{ mode: 'light' \}", "theme: { mode: 'dark' }", content)
content = re.sub(r"borderColor: '#f1f5f9'", "borderColor: '#334155'", content)
content = re.sub(r"tooltip: \{ theme: 'light'", "tooltip: { theme: 'dark'", content)

# Ensure chart backgrounds match the new theme
content = re.sub(r"background: 'transparent'", "background: 'transparent'", content)

with open('dashboards_mockups.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Transformations applied.")
