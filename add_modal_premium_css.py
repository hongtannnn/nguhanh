css_content = r'''
/* Customizing CD Modal to look more premium */
.cd-modal { background: #faf8f5; border: 1px solid rgba(0,0,0,0.05); }
.cd-modal .auth-hdr { flex-direction: column; text-align: center; gap: 12px; border-bottom: none; padding-bottom: 16px; margin-bottom: 32px; position: relative; }
.cd-modal .auth-hdr::after { content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 40px; height: 2px; background: var(--green-main); opacity: 0.3; }
.cd-modal .auth-hdr h3 { font-size: 32px; color: var(--green-dark); }
.cd-modal .auth-hdr p { font-size: 14.5px; max-width: 320px; margin: 0 auto; color: #8a7a6a; }
.cd-modal .form-group { margin-bottom: 20px; }
.cd-modal .form-input { background: rgba(255,255,255,0.7); border: 1px solid rgba(0,0,0,0.08); padding: 14px 16px; font-size: 14.5px; }
.cd-modal .form-input:focus { background: #fff; border-color: var(--green-main); box-shadow: 0 0 0 4px rgba(45,89,64,0.08); }
.cd-modal .btn-primary { margin-top: 24px !important; padding: 14px; font-size: 15px; border-radius: 12px; }
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
