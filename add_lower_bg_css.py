css_content = r'''
/* --- LOWER SECTIONS BACKGROUND AESTHETICS --- */
#nguhanh {
  background: linear-gradient(180deg, #f2eae4 0%, #ece5de 100%) !important;
  border: none !important;
  position: relative;
}
#nguhanh::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle at 80% 80%, rgba(200,180,170,0.15) 0%, transparent 60%);
}

#testimonials {
  background: linear-gradient(180deg, #ece5de 0%, #e6dfd6 100%) !important;
  position: relative;
}
#testimonials::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle at 20% 50%, rgba(190,175,160,0.15) 0%, transparent 60%);
}

#congdong {
  background-color: transparent !important;
  background-image: radial-gradient(circle, rgba(0,0,0,0.04) 1.5px, transparent 1.5px), linear-gradient(180deg, #e6dfd6 0%, #e1d9ce 100%) !important;
  border-top: none !important;
}

#banggia {
  background: linear-gradient(180deg, #e1d9ce 0%, #dbd2c5 100%) !important;
  border: none !important;
  position: relative;
}
#banggia::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle at 80% 20%, rgba(180,165,150,0.15) 0%, transparent 60%);
}

/* Ensure footer blends perfectly */
footer {
  background: #dbd2c5 !important;
  border-top: 1px solid rgba(0,0,0,0.05);
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
