css_content = r'''
/* ─── CỘNG ĐỒNG ─── */
#congdong { padding: 100px 0; background: var(--bg-main); border-top: 1px solid rgba(0,0,0,0.05); }
.congdong-hdr { text-align: center; margin-bottom: 60px; }
.congdong-hdr h2 { font-size: clamp(32px, 3.5vw, 48px); font-weight: 500; color: var(--green-dark); line-height: 1.2; margin-bottom: 12px; }
.congdong-hdr h2 em { font-style: italic; color: var(--green-main); font-family: var(--f-italic); }
.congdong-hdr p { font-size: 15px; color: #7a6a5a; }

.congdong-masonry { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto; align-items: start; }
.cd-col { display: flex; flex-direction: column; gap: 24px; }
.cd-card { background: var(--cream-card); padding: 28px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); transition: transform 0.3s ease, box-shadow 0.3s ease; }
.cd-card:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.06); }
.cd-tag { display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--green-dark); margin-bottom: 16px; background: rgba(0,0,0,0.04); padding: 4px 10px; border-radius: 20px; }
.cd-text { font-family: var(--f-italic); font-size: 17px; line-height: 1.6; color: var(--brown); margin-bottom: 20px; font-style: italic; }
.cd-author { font-size: 12px; color: #9a8a7a; text-align: right; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 12px; }

@media (max-width: 900px) {
  .congdong-masonry { grid-template-columns: repeat(2, 1fr); }
  .cd-col:nth-child(3) { display: none; }
}
@media (max-width: 600px) {
  .congdong-masonry { grid-template-columns: 1fr; }
  .cd-col { margin-top: 0 !important; }
}

.cd-modal { max-width: 460px; padding: 40px; }
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

js_content = r'''
/* ─── CỘNG ĐỒNG ─── */
function openCongDongModal() {
  const modal = document.getElementById('cdModal');
  if (modal) {
    modal.classList.add('show');
    document.querySelector('.auth-form').style.display = 'block';
    document.getElementById('cd-success').style.display = 'none';
  }
}
function closeCongDongModal() {
  const modal = document.getElementById('cdModal');
  if (modal) {
    modal.classList.remove('show');
    setTimeout(() => {
        document.getElementById('cd-text').value = '';
        document.getElementById('cd-author').value = '';
    }, 300);
  }
}
function submitCongDong(e) {
  e.preventDefault();
  // Ẩn form, hiện success
  document.querySelector('.auth-form').style.display = 'none';
  document.getElementById('cd-success').style.display = 'block';
}
'''

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(js_content)
