import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Navbar Logo
old_logo = '''  <nav id="navbar">
    <a href="#" class="nav-logo">
      <svg class="nav-logo-icon" viewBox="0 0 40 40" fill="none">
        <circle cx="20" cy="20" r="18.5" stroke="currentColor" stroke-width="1.2" opacity=".5"/>
        <circle cx="20" cy="8" r="2" fill="currentColor"/>
        <path d="M20 10 Q28 20 20 30 Q12 20 20 10Z" stroke="currentColor" stroke-width="1" fill="currentColor" fill-opacity=".15"/>
        <path d="M10 28 Q20 22 30 28" stroke="currentColor" stroke-width="1" fill="none" opacity=".35"/>
      </svg>
      Ngũ Hành
    </a>'''

new_logo = '''  <nav id="navbar">
    <a href="#" class="nav-logo">
      <img src="photos/logo.jpg" alt="Ngũ Hành" style="height:48px; border-radius:50%; box-shadow:0 2px 10px rgba(0,0,0,0.1)">
    </a>'''

content = content.replace(old_logo, new_logo)

# 2. Add switchViewerImg function in script
script_addition = '''// ─── INBOX INTERACTIVE ───
function switchViewerImg(src) {
  event.stopPropagation();
  const vi = document.getElementById('inboxViewerImg');
  vi.classList.add('switching');
  setTimeout(()=>{
    vi.src = src;
    vi.classList.remove('switching');
  }, 240);
}

function selectInboxItem(item){'''

content = content.replace('''// ─── INBOX INTERACTIVE ───
function selectInboxItem(item){''', script_addition)

# 3. Replace tea tags
old_tags = '''              <div class="inbox-detail-tags">
              <span class="inbox-tag">🌿 CALM (Mộc)</span>
              <span class="inbox-tag">🔥 RELEASE (Hỏa)</span>
              <span class="inbox-tag">⚖️ BALANCE (Thổ)</span>
              <span class="inbox-tag">🤍 COMFORT (Kim)</span>
              <span class="inbox-tag">💧 RESTORE (Thủy)</span>
              <span class="inbox-tag">100% Organic</span>
              </div>'''

new_tags = '''              <div class="inbox-detail-tags">
              <span class="inbox-tag" onclick="switchViewerImg('photos/moc.jpg')" style="cursor:pointer;transition:0.3s" onmouseover="this.style.background='var(--green-main)';this.style.color='white'" onmouseout="this.style.background='var(--cream-card)';this.style.color='#7a6a5a'">🌿 CALM (Mộc)</span>
              <span class="inbox-tag" onclick="switchViewerImg('photos/hoa.jpg')" style="cursor:pointer;transition:0.3s" onmouseover="this.style.background='var(--hoa)';this.style.color='white'" onmouseout="this.style.background='var(--cream-card)';this.style.color='#7a6a5a'">🔥 RELEASE (Hỏa)</span>
              <span class="inbox-tag" onclick="switchViewerImg('photos/tho.jpg')" style="cursor:pointer;transition:0.3s" onmouseover="this.style.background='var(--tho)';this.style.color='white'" onmouseout="this.style.background='var(--cream-card)';this.style.color='#7a6a5a'">⚖️ BALANCE (Thổ)</span>
              <span class="inbox-tag" onclick="switchViewerImg('photos/kim.jpg')" style="cursor:pointer;transition:0.3s" onmouseover="this.style.background='var(--kim)';this.style.color='white'" onmouseout="this.style.background='var(--cream-card)';this.style.color='#7a6a5a'">🤍 COMFORT (Kim)</span>
              <span class="inbox-tag" onclick="switchViewerImg('photos/thuy.jpg')" style="cursor:pointer;transition:0.3s" onmouseover="this.style.background='var(--thuy)';this.style.color='white'" onmouseout="this.style.background='var(--cream-card)';this.style.color='#7a6a5a'">💧 RESTORE (Thủy)</span>
              <span class="inbox-tag">100% Organic</span>
              </div>'''

content = content.replace(old_tags, new_tags)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
