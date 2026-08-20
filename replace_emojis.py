import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to replace the 5 emotion buttons
html = re.sub(r'<button class="emotion-btn" data-h="moc" onclick="selectEmotion\(this\)">.*?<span class="e-label">Lo \nâu<br>Overthinking</span></button>', 
              '<button class="emotion-btn" data-h="moc" onclick="selectEmotion(this)">\n                            <div class="e-blob" data-h="moc"></div>\n                            <span class="e-label">Lo âu<br>Overthinking</span>\n                        </button>', html, flags=re.DOTALL)

html = re.sub(r'<button class="emotion-btn" data-h="hoa" onclick="selectEmotion\(this\)">.*?<span class="e-label">Căng thẳng<br>Dồn \nnén</span></button>',
              '<button class="emotion-btn" data-h="hoa" onclick="selectEmotion(this)">\n                            <div class="e-blob" data-h="hoa"></div>\n                            <span class="e-label">Căng thẳng<br>Dồn nén</span>\n                        </button>', html, flags=re.DOTALL)

html = re.sub(r'<button class="emotion-btn" data-h="tho" onclick="selectEmotion\(this\)">.*?<span class="e-label">Mất \nphương<br>hướng</span></button>',
              '<button class="emotion-btn" data-h="tho" onclick="selectEmotion(this)">\n                            <div class="e-blob" data-h="tho"></div>\n                            <span class="e-label">Mất phương<br>hướng</span>\n                        </button>', html, flags=re.DOTALL)

html = re.sub(r'<button class="emotion-btn" data-h="kim" onclick="selectEmotion\(this\)">.*?<span class="e-label">Buồn bã<br>Cô \nđơn</span></button>',
              '<button class="emotion-btn" data-h="kim" onclick="selectEmotion(this)">\n                            <div class="e-blob" data-h="kim"></div>\n                            <span class="e-label">Buồn bã<br>Cô đơn</span>\n                        </button>', html, flags=re.DOTALL)

html = re.sub(r'<button class="emotion-btn" data-h="thuy" onclick="selectEmotion\(this\)">.*?<span class="e-label">Kiệt \nsức<br>Burnout</span></button>',
              '<button class="emotion-btn" data-h="thuy" onclick="selectEmotion(this)">\n                            <div class="e-blob" data-h="thuy"></div>\n                            <span class="e-label">Kiệt sức<br>Burnout</span>\n                        </button>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
