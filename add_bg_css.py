css_content = r'''
/* --- EDITORIAL BACKGROUND AESTHETICS --- */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.035;
  mix-blend-mode: multiply;
}

#cauchuyen {
  background: linear-gradient(170deg, #fdfaf6 0%, #f4efe9 100%) !important;
  position: relative;
}
#cauchuyen::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle at 80% 20%, rgba(220,195,170,0.15) 0%, transparent 50%);
}

#nghithuc.ritual-light {
  background: linear-gradient(180deg, #f4efe9 0%, #edf1eb 100%) !important;
  position: relative;
  border-top: none !important;
}
#nghithuc.ritual-light::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle at 20% 80%, rgba(181,195,176,0.2) 0%, transparent 60%);
}

#tronghop {
  background: linear-gradient(180deg, #edf1eb 0%, #f2eae4 100%) !important;
  position: relative;
}
#tronghop::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(circle at 50% 50%, rgba(210,185,170,0.15) 0%, transparent 60%);
}

/* Ambient glow for images */
.story-img-wrap::before {
  content: ''; position: absolute; inset: -40px; 
  background: radial-gradient(circle, rgba(160,180,150,0.25) 0%, transparent 70%);
  z-index: -1; pointer-events: none; filter: blur(30px);
}

.inbox-viewer {
  position: relative;
}
.inbox-viewer::before {
  content: ''; position: absolute; inset: -40px; 
  background: radial-gradient(circle, rgba(180,160,150,0.2) 0%, transparent 70%);
  z-index: -1; pointer-events: none; filter: blur(40px);
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
