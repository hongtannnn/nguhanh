import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix header alignment
old_header = '''<img src="photos/logo.png" alt="Ngũ Hành Logo"
                style="height:40px; border-radius:50%; box-shadow:0 2px 10px rgba(0,0,0,0.1)">
            Ngũ Hành <span style="font-family: var(--f-body); font-weight: 400; font-size: 15px; opacity: 0.85;">·
                Self-Care</span>'''
new_header = '''<img src="photos/logo.png" alt="Ngũ Hành Logo"
                style="height:40px; border-radius:50%; box-shadow:0 2px 10px rgba(0,0,0,0.1)">
            <div style="display:flex;align-items:center;gap:6px">Ngũ Hành <span style="font-family: var(--f-body); font-weight: 400; font-size: 15px; opacity: 0.85; transform: translateY(1px);">· Self-Care</span></div>'''
content = content.replace(old_header, new_header)

footer_start = content.find('<div class="f-brand-name">')
footer_end = content.find('</div>\n                <div>\n                    <h4 class="f-col-title">Khám phá</h4>')

if footer_start != -1 and footer_end != -1:
    footer_col1 = content[footer_start:footer_end]
    
    # Replace the social block and add newsletter
    new_col1 = '''<div class="f-brand-name"><img src="photos/logo.png" alt="Ngũ Hành"
                            style="width:26px; height:26px; border-radius:50%"> Ngũ Hành · Self-Care</div>
                    <p class="f-brand-desc">Chậm lại một chút. Một cuộc đời tốt đẹp không được xây bằng những buổi tối
                        bồn chồn. Chúng mình gói ghém 15 phút mỗi ngày để bạn về được với chính mình.</p>
                    
                    <div class="f-newsletter">
                        <h4>Nhận bản tin chăm sóc cảm xúc</h4>
                        <form onsubmit="event.preventDefault()">
                            <input type="email" placeholder="Email của bạn" required>
                            <button type="submit">Đăng ký</button>
                        </form>
                    </div>

                    <div class="f-socials">
                        <a href="#" class="f-social-btn" aria-label="Instagram"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
                            </svg></a>
                        <a href="#" class="f-social-btn" aria-label="TikTok"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.32 6.32 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V9.07a8.16 8.16 0 004.77 1.52v-3.4a4.85 4.85 0 01-1-.5z"/>
                            </svg></a>
                        <a href="#" class="f-social-btn" aria-label="Facebook"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                            </svg></a>
                        <a href="#" class="f-social-btn" aria-label="Spotify"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.54.659.301 1.02zm1.44-3.3c-.301.42-.84.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.84.241 1.2zM19.08 9.3C15.24 7.02 8.82 6.84 5.1 7.98c-.6.18-1.2-.18-1.38-.72-.18-.6.18-1.2.72-1.38 4.32-1.26 11.28-1.02 15.721 1.62.54.3.72.96.42 1.5-.24.54-.9.72-1.5.3z"/>
                            </svg></a>
                    </div>'''
    content = content.replace(footer_col1, new_col1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''\n
/* FOOTER NEWSLETTER */
.f-newsletter {
    margin-bottom: 24px;
}
.f-newsletter h4 {
    font-size: 14px;
    margin-bottom: 12px;
    font-weight: 500;
    font-family: var(--f-display);
}
.f-newsletter form {
    display: flex;
    gap: 8px;
    max-width: 320px;
}
.f-newsletter input {
    flex: 1;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 100px;
    padding: 10px 16px;
    color: white;
    font-family: var(--f-body);
    font-size: 13px;
    outline: none;
    transition: var(--t);
}
.f-newsletter input::placeholder {
    color: rgba(255,255,255,0.4);
}
.f-newsletter input:focus {
    border-color: rgba(255,255,255,0.4);
    background: rgba(255,255,255,0.08);
}
.f-newsletter button {
    background: #C8A04A;
    color: #111;
    font-weight: 500;
    font-family: var(--f-body);
    font-size: 13px;
    border: none;
    border-radius: 100px;
    padding: 0 20px;
    cursor: pointer;
    transition: opacity 0.3s;
}
.f-newsletter button:hover {
    opacity: 0.85;
}
/* Ensure logos in footer are crisp */
.f-social-btn svg {
    filter: none !important;
}
''')

print('Success')
