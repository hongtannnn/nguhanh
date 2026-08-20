css_content = r'''
/* ─── WEB CHECK-IN REDESIGN ─── */
.ci-card { padding: 60px 40px; max-width: 900px; box-shadow: 0 40px 100px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.15); }
.ci-step-label { justify-content: center; font-size: 12px; margin-bottom: 24px; }
.ci-step-label::before { display: none; }
.ci-question { font-size: 36px; margin-bottom: 48px; }

.emotion-grid { gap: 16px; margin-bottom: 48px; }

.emotion-btn { padding: 32px 16px 24px; border-radius: 24px; border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02); overflow: hidden; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
.emotion-btn:hover { background: rgba(255,255,255,0.06); border-color: rgba(255,255,255,0.2); transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
.emotion-btn.selected { border-width: 2px; transform: translateY(-8px); box-shadow: 0 20px 50px rgba(0,0,0,0.3); }

.e-label { font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; z-index: 2; position: relative; margin-top: 16px; display: block; color: rgba(255,255,255,0.9); }
.emotion-btn:hover .e-label { color: #fff; }

/* Abstract Blobs */
.e-blob { width: 64px; height: 64px; margin: 0 auto; border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; transition: all 0.5s ease; animation: morph 6s ease-in-out infinite both alternate; z-index: 2; position: relative; }
@keyframes morph {
  0% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
  34% { border-radius: 70% 30% 50% 50% / 30% 30% 70% 70%; }
  67% { border-radius: 100% 60% 60% 100% / 100% 100% 60% 60%; }
  100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
}

.e-blob[data-h="moc"] { background: linear-gradient(135deg, #a8d5ba 0%, #456b4e 100%); box-shadow: 0 0 20px rgba(168,213,186,0.3); }
.e-blob[data-h="hoa"] { background: linear-gradient(135deg, #ff9a76 0%, #ba6341 100%); box-shadow: 0 0 20px rgba(255,154,118,0.3); }
.e-blob[data-h="tho"] { background: linear-gradient(135deg, #e6cd98 0%, #a07840 100%); box-shadow: 0 0 20px rgba(230,205,152,0.3); }
.e-blob[data-h="kim"] { background: linear-gradient(135deg, #f2ede6 0%, #a89f91 100%); box-shadow: 0 0 20px rgba(242,237,230,0.3); }
.e-blob[data-h="thuy"] { background: linear-gradient(135deg, #8ab4f8 0%, #3d5c7a 100%); box-shadow: 0 0 20px rgba(138,180,248,0.3); }

/* Hover effects for blobs */
.emotion-btn:hover .e-blob[data-h="moc"] { box-shadow: 0 0 40px rgba(168,213,186,0.6); transform: scale(1.1); animation-duration: 3s; }
.emotion-btn:hover .e-blob[data-h="hoa"] { box-shadow: 0 0 40px rgba(255,154,118,0.6); transform: scale(1.1); animation-duration: 3s; }
.emotion-btn:hover .e-blob[data-h="tho"] { box-shadow: 0 0 40px rgba(230,205,152,0.6); transform: scale(1.1); animation-duration: 3s; }
.emotion-btn:hover .e-blob[data-h="kim"] { box-shadow: 0 0 40px rgba(242,237,230,0.6); transform: scale(1.1); animation-duration: 3s; }
.emotion-btn:hover .e-blob[data-h="thuy"] { box-shadow: 0 0 40px rgba(138,180,248,0.6); transform: scale(1.1); animation-duration: 3s; }

.emotion-btn.selected .e-blob { transform: scale(1.15); }
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
