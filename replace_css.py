import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The old CSS block starts around /* ── RITUAL ── */ and goes until the next comment
old_css_regex = r'/\* ── RITUAL ── \*/.*?/\* ── INBOX ── \*/'

new_css = r'''/* ── RITUAL (ZIGZAG LIGHT THEME) ── */
#nghithuc.ritual-light { padding: 130px 0; background: var(--bg-main); position: relative; overflow: hidden; border-top: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); }
.ritual-light .ritual-hdr { text-align: center; margin-bottom: 100px; }
.ritual-light .section-tag-line { display: flex; align-items: center; justify-content: center; gap: 16px; margin-bottom: 24px; color: var(--brown-light); font-size: 11px; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.ritual-light .section-tag-line::before, .ritual-light .section-tag-line::after { content: ''; width: 40px; height: 1px; background: currentColor; opacity: 0.4; }
.ritual-light h2 { font-size: clamp(34px, 4vw, 54px); font-weight: 500; color: var(--green-dark); line-height: 1.18; margin-bottom: 16px; }
.ritual-light h2 em { font-style: italic; color: var(--green-main); font-family: var(--f-italic); }
.ritual-light p { color: #7a6a5a; font-size: 15px; font-weight: 400; max-width: 540px; margin: 0 auto; line-height: 1.7; }

.ritual-timeline { position: relative; max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 60px; }
.rt-line { position: absolute; top: 0; bottom: 0; left: 50%; transform: translateX(-50%); width: 1px; background: rgba(0,0,0,0.08); z-index: 1; }

.rt-step { display: flex; align-items: center; justify-content: space-between; position: relative; z-index: 2; width: 100%; }
.rt-img-side, .rt-text-side { width: 45%; }

/* Default (Image Left, Text Right) */
.rt-text-side { padding-left: 20px; }
.rt-img-side { display: flex; justify-content: flex-end; padding-right: 20px; }

/* Right Step (Text Left, Image Right) */
.rt-step.right { flex-direction: row-reverse; }
.rt-step.right .rt-text-side { padding-left: 0; padding-right: 20px; text-align: right; }
.rt-step.right .rt-img-side { justify-content: flex-start; padding-right: 0; padding-left: 20px; }
.rt-step.right .rt-title { justify-content: flex-end; }
.rt-step.right .rt-num { right: 20px; left: auto; }

.rt-dot { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 48px; height: 48px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(0,0,0,0.04); z-index: 3; }
.rt-dot span { width: 8px; height: 8px; background: var(--green-main); border-radius: 50%; }

.rt-img-wrapper { position: relative; border-radius: 20px; overflow: hidden; width: 100%; max-width: 380px; aspect-ratio: 4/3; box-shadow: 0 10px 30px rgba(0,0,0,0.06); }
.rt-img-wrapper img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
.rt-step:hover .rt-img-wrapper img { transform: scale(1.04); }

.rt-img-tag { position: absolute; top: 16px; left: 16px; display: flex; gap: 8px; }
.rt-tag-label { background: #dce5df; color: var(--green-dark); padding: 4px 10px; border-radius: 20px; font-size: 10px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.rt-tag-time { background: #fff; color: #555; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 500; display: flex; align-items: center; gap: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }

.rt-text-side { position: relative; }
.rt-num { font-family: var(--f-display); font-size: 100px; color: var(--brown-light); opacity: 0.2; line-height: 0.8; position: absolute; top: -40px; left: 20px; z-index: -1; pointer-events: none; }
.rt-title { font-size: 22px; font-weight: 500; color: var(--green-dark); margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
.rt-icon { width: 32px; height: 32px; border-radius: 50%; background: #fff; display: flex; align-items: center; justify-content: center; font-size: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.04); }
.rt-desc { font-size: 14.5px; color: #7a6a5a; line-height: 1.7; font-weight: 400; }

@media (max-width: 768px) {
  .rt-line { display: none; }
  .rt-dot { display: none; }
  .rt-step { flex-direction: column !important; gap: 24px; text-align: center; }
  .rt-img-side, .rt-text-side { width: 100%; padding: 0 !important; }
  .rt-step.right .rt-text-side { text-align: center; }
  .rt-title { justify-content: center !important; }
  .rt-num { left: 50% !important; transform: translateX(-50%); top: -30px; }
  .rt-img-wrapper { max-width: 100%; }
}

/* ── INBOX ── */'''

if re.search(old_css_regex, css, re.DOTALL):
    css = re.sub(old_css_regex, new_css, css, flags=re.DOTALL)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS Replaced successfully")
else:
    print("Could not find old CSS regex")
