
# SVG Line Art cho từng cảm xúc
svg_moc = '<div class="e-svg-icon" data-h="moc"><svg viewBox="0 0 60 60" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="icon-path" d="M30 30 C36 26 42 28 42 34 C42 42 34 46 26 43 C18 40 14 32 16 24 C18 16 26 10 34 10 C44 10 52 18 52 30 C52 44 42 54 28 54"/></svg></div>'

svg_hoa = '<div class="e-svg-icon" data-h="hoa"><svg viewBox="0 0 60 60" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="icon-path" points="18,12 42,12 18,20 42,20 18,28 42,28 18,36 42,36 18,44 42,44 18,52 42,52"/></svg></div>'

svg_tho = '<div class="e-svg-icon" data-h="tho"><svg viewBox="0 0 60 60" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle class="icon-fill" cx="30" cy="30" r="3" fill="currentColor" stroke="none"/><line class="icon-path" x1="30" y1="30" x2="16" y2="16"/><polyline class="icon-path" points="22,16 16,16 16,22"/><line class="icon-path" x1="30" y1="30" x2="44" y2="16"/><polyline class="icon-path" points="38,16 44,16 44,22"/><line class="icon-path" x1="30" y1="30" x2="16" y2="44"/><polyline class="icon-path" points="16,38 16,44 22,44"/><line class="icon-path" x1="30" y1="30" x2="44" y2="44"/><polyline class="icon-path" points="44,38 44,44 38,44"/><line class="icon-path" x1="30" y1="30" x2="50" y2="28"/><polyline class="icon-path" points="44,24 50,28 44,32"/></svg></div>'

svg_kim = '<div class="e-svg-icon" data-h="kim"><svg viewBox="0 0 60 60" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="icon-path" d="M30 8 C30 8 46 30 46 40 C46 49.4 38.8 55 30 55 C21.2 55 14 49.4 14 40 C14 30 30 8 30 8Z"/></svg></div>'

svg_thuy = '<div class="e-svg-icon" data-h="thuy"><svg viewBox="0 0 60 60" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect class="icon-path" x="22" y="30" width="16" height="20" rx="2"/><line class="icon-path" x1="30" y1="30" x2="30" y2="24"/><path class="icon-path" d="M30 24 C28 20 29 17 30 15 C31 17 32 20 30 24Z"/><line class="icon-path" x1="25" y1="37" x2="35" y2="37"/><line class="icon-path" x1="25" y1="43" x2="35" y2="43"/><path class="icon-path" d="M22 36 C19 39 19 44 21 46"/></svg></div>'

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="e-aura aura-moc"></div>', svg_moc)
content = content.replace('<div class="e-aura aura-hoa"></div>', svg_hoa)
content = content.replace('<div class="e-aura aura-tho"></div>', svg_tho)
content = content.replace('<div class="e-aura aura-kim"></div>', svg_kim)
content = content.replace('<div class="e-aura aura-thuy"></div>', svg_thuy)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated")

# CSS cho SVG icons
css = """

/* ===== SVG LINE ART EMOTION ICONS ===== */
.e-svg-icon {
  width: 56px;
  height: 56px;
  margin: 0 auto 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: filter 0.4s ease, transform 0.4s ease;
  position: relative;
  z-index: 2;
}

.e-svg-icon svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

/* Màu mặc định (mờ) theo từng Hành */
.e-svg-icon[data-h="moc"] { color: rgba(100, 160, 120, 0.5); }
.e-svg-icon[data-h="hoa"] { color: rgba(210, 100, 60, 0.5); }
.e-svg-icon[data-h="tho"] { color: rgba(185, 150, 70, 0.5); }
.e-svg-icon[data-h="kim"] { color: rgba(190, 180, 170, 0.5); }
.e-svg-icon[data-h="thuy"] { color: rgba(80, 140, 210, 0.5); }

/* Đường nét mặc định luôn hiển thị */
.icon-path {
  stroke: currentColor;
  stroke-dasharray: 600;
  stroke-dashoffset: 0;
}

.icon-fill {
  fill: currentColor;
  transition: fill 0.4s ease;
}

/* Hover: sáng lên + glow + animation vẽ lại nét */
.emotion-btn:hover .e-svg-icon[data-h="moc"] { color: rgba(110, 185, 135, 1); filter: drop-shadow(0 0 10px rgba(110, 185, 135, 0.55)); }
.emotion-btn:hover .e-svg-icon[data-h="hoa"] { color: rgba(225, 100, 55, 1); filter: drop-shadow(0 0 10px rgba(225, 100, 55, 0.55)); }
.emotion-btn:hover .e-svg-icon[data-h="tho"] { color: rgba(200, 165, 72, 1); filter: drop-shadow(0 0 10px rgba(200, 165, 72, 0.55)); }
.emotion-btn:hover .e-svg-icon[data-h="kim"] { color: rgba(218, 208, 198, 1); filter: drop-shadow(0 0 10px rgba(218, 208, 198, 0.45)); }
.emotion-btn:hover .e-svg-icon[data-h="thuy"] { color: rgba(80, 155, 238, 1); filter: drop-shadow(0 0 10px rgba(80, 155, 238, 0.55)); }

.emotion-btn:hover .icon-path {
  animation: svg-redraw 0.9s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes svg-redraw {
  0% { stroke-dashoffset: 600; }
  100% { stroke-dashoffset: 0; }
}

/* Selected */
.emotion-btn.selected .e-svg-icon[data-h="moc"] { color: #64b478; filter: drop-shadow(0 0 16px rgba(100, 180, 130, 0.85)); }
.emotion-btn.selected .e-svg-icon[data-h="hoa"] { color: #d9614a; filter: drop-shadow(0 0 16px rgba(217, 97, 74, 0.85)); }
.emotion-btn.selected .e-svg-icon[data-h="tho"] { color: #c8a04a; filter: drop-shadow(0 0 16px rgba(200, 160, 74, 0.85)); }
.emotion-btn.selected .e-svg-icon[data-h="kim"] { color: #d8d0c8; filter: drop-shadow(0 0 16px rgba(216, 208, 200, 0.75)); }
.emotion-btn.selected .e-svg-icon[data-h="thuy"] { color: #5096eb; filter: drop-shadow(0 0 16px rgba(80, 150, 235, 0.85)); }

.emotion-btn:hover .e-svg-icon,
.emotion-btn.selected .e-svg-icon {
  transform: scale(1.12);
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("CSS updated")
