css_content = r'''
/* ─── MODAL TỔNG HỢP ─── */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 9999; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.3s; padding: 20px; }
.modal-overlay.show { opacity: 1; pointer-events: auto; }
.modal-content { background: var(--cream); border-radius: 28px; width: 100%; position: relative; transform: scale(0.94); transition: transform 0.38s; box-shadow: 0 30px 80px rgba(0,0,0,0.25); }
.modal-overlay.show .modal-content { transform: scale(1); }
.modal-close { position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.05); border: none; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #555; transition: background 0.2s; }
.modal-close:hover { background: rgba(0,0,0,0.1); }
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
