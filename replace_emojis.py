import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

grid_start = content.find('<div class="emotion-grid">')
grid_end = content.find('</div>', grid_start + 26)
# wait, there are nested divs or buttons. The emotions grid ends with a </div> which closes the grid.
# The grid has buttons, and then a </div>
grid_end = content.find('</div>\n                </div>', grid_start)
if grid_end == -1:
    grid_end = content.find('</div>', grid_start + 1000)

grid_content = content[grid_start:grid_end]

auras = ['aura-moc', 'aura-hoa', 'aura-tho', 'aura-kim', 'aura-thuy']
def replace_aura(match):
    if not auras:
        return match.group(0)
    aura = auras.pop(0)
    return f'<div class="e-aura {aura}"></div>'

new_grid_content = re.sub(r'<span[^>]*class="e-emoji"[^>]*>.*?</span>', replace_aura, grid_content, flags=re.DOTALL)

content = content[:grid_start] + new_grid_content + content[grid_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

css_content = """
/* EMOTION AURAS */
.e-aura {
    width: 36px;
    height: 36px;
    margin: 0 auto 12px;
    border-radius: 50%;
    position: relative;
}

/* Lo âu - Tangled/Swirling (Mộc) */
.aura-moc {
    background: conic-gradient(from 0deg, var(--moc-bg), var(--moc), var(--moc-bg));
    animation: spin 3s linear infinite;
    filter: blur(3px);
}

/* Căng thẳng - Pulsing Fire (Hỏa) */
.aura-hoa {
    background: radial-gradient(circle, var(--hoa) 20%, transparent 70%);
    animation: pulse-fire 1s ease-in-out infinite alternate;
    box-shadow: 0 0 15px var(--hoa);
}

/* Mất phương hướng - Blurred/Scattered (Thổ) */
.aura-tho {
    background: repeating-linear-gradient(45deg, var(--tho), var(--tho) 2px, transparent 2px, transparent 6px);
    border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
    animation: morph-tho 4s ease-in-out infinite alternate;
    opacity: 0.7;
}

/* Buồn bã - Heavy drop / fading (Kim) */
.aura-kim {
    background: linear-gradient(to bottom, transparent, var(--kim) 80%);
    border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
    animation: sway-kim 3s ease-in-out infinite alternate;
}

/* Kiệt sức - Fading ripple (Thủy) */
.aura-thuy {
    border: 2px solid var(--thuy);
    background: transparent;
    animation: ripple-thuy 2s infinite cubic-bezier(0.1, 0.5, 0.3, 1);
}

@keyframes spin { 100% { transform: rotate(360deg); } }
@keyframes pulse-fire { 0% { transform: scale(0.9); opacity: 0.8; } 100% { transform: scale(1.1); opacity: 1; } }
@keyframes morph-tho { 
    0% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; } 
    100% { border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%; transform: rotate(10deg); } 
}
@keyframes sway-kim { 
    0% { transform: translateY(-4px); opacity: 0.8; } 
    100% { transform: translateY(4px); opacity: 0.4; } 
}
@keyframes ripple-thuy { 
    0% { transform: scale(0.6); opacity: 1; } 
    100% { transform: scale(1.4); opacity: 0; } 
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("Done")
