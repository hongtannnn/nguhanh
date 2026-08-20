import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all styles
styles = []
def replace_style(match):
    styles.append(match.group(1))
    return ''

content = re.sub(r'<style>(.*?)</style>', replace_style, content, flags=re.DOTALL)

# Add link tag in head if not exists
if '</head>' in content:
    content = content.replace('</head>', '  <link rel="stylesheet" href="style.css">\n</head>', 1)

# Extract all scripts
scripts = []
def replace_script(match):
    # Only match script tags with content and no src
    if 'src=' not in match.group(0):
        scripts.append(match.group(1))
        return ''
    return match.group(0)

content = re.sub(r'<script\b[^>]*>(.*?)</script>', replace_script, content, flags=re.DOTALL)

# Add script tag before </body>
if '</body>' in content:
    content = content.replace('</body>', '<script src="script.js"></script>\n</body>', 1)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write('\n'.join(styles))

with open('script.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(scripts))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
