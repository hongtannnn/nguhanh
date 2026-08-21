/* ═══════════════════════════════════════════════════
   NGŨ HÀNH — ANIMATIONS JAVASCRIPT SYSTEM
   ═══════════════════════════════════════════════════ */

(function () {
  'use strict';

  const isMobile = () => window.innerWidth < 768;
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ─── 1. SCROLL PROGRESS BAR ───
  const progressBar = document.createElement('div');
  progressBar.id = 'scroll-progress';
  document.body.prepend(progressBar);

  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const total = document.documentElement.scrollHeight - window.innerHeight;
    progressBar.style.width = (scrolled / total * 100).toFixed(2) + '%';
  }, { passive: true });


  // ─── 2. CUSTOM CURSOR ───
  if (!isMobile() && !prefersReduced) {
    const dot  = document.createElement('div');
    const ring = document.createElement('div');
    dot.className  = 'cursor-dot';
    ring.className = 'cursor-ring';
    document.body.appendChild(dot);
    document.body.appendChild(ring);

    let mx = -100, my = -100; // mouse
    let rx = -100, ry = -100; // ring (lagged)

    window.addEventListener('mousemove', e => {
      mx = e.clientX; my = e.clientY;
      dot.style.left  = mx + 'px';
      dot.style.top   = my + 'px';
    });

    // lerp the ring
    function lerpCursor() {
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + 'px';
      ring.style.top  = ry + 'px';
      requestAnimationFrame(lerpCursor);
    }
    lerpCursor();

    // hover state on interactive elements
    const interactives = 'a, button, [role="button"], .emotion-btn, .inbox-item, .hanh-tab, .price-card';
    document.addEventListener('mouseover', e => {
      if (e.target.closest(interactives)) ring.classList.add('hover');
    });
    document.addEventListener('mouseout', e => {
      if (e.target.closest(interactives)) ring.classList.remove('hover');
    });
    document.addEventListener('mousedown', () => ring.classList.add('clicking'));
    document.addEventListener('mouseup',   () => ring.classList.remove('clicking'));
  }


  // ─── 3. AMBIENT BLOBS — CHECK-IN ───
  const checkinSection = document.getElementById('checkin');
  if (checkinSection && !prefersReduced) {
    const blobColors = {
      moc:  '#64b478',
      hoa:  '#d9614a',
      tho:  '#c8a04a',
      kim:  '#d8d0c8',
      thuy: '#5096eb',
      default: ['#64b478', '#456b4e']
    };

    const b1 = document.createElement('div');
    const b2 = document.createElement('div');
    const b3 = document.createElement('div');
    b1.className = 'ci-blob ci-blob-1';
    b2.className = 'ci-blob ci-blob-2';
    b3.className = 'ci-blob ci-blob-3';
    b1.style.background = blobColors.moc;
    b2.style.background = '#456b4e';
    b3.style.background = '#C8A04A';
    checkinSection.prepend(b3);
    checkinSection.prepend(b2);
    checkinSection.prepend(b1);

    // Activate when in view
    const blobObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        [b1, b2, b3].forEach(b => b.classList.toggle('visible-blob', e.isIntersecting));
      });
    }, { threshold: 0.1 });
    blobObs.observe(checkinSection);

    // Change color when emotion selected
    const origSelectEmotion = window.selectEmotion;
    window.selectEmotion = function(btn) {
      if (origSelectEmotion) origSelectEmotion(btn);
      const h = btn.dataset.h;
      const c = blobColors[h] || blobColors.moc;
      b1.style.background = c;
      b2.style.background = c;
      b3.style.background = c;
    };
  }


  // ─── 4. FLOATING KANJI — NGŨ HÀNH ───
  const nguhanhSection = document.getElementById('nguhanh');
  if (nguhanhSection && !prefersReduced) {
    const kanjis = [
      { char: '木', color: 'var(--moc)', x: 5,  delay: 0,   duration: 24 },
      { char: '火', color: 'var(--hoa)', x: 22, delay: 5,   duration: 20 },
      { char: '土', color: 'var(--tho)', x: 48, delay: 2,   duration: 28 },
      { char: '金', color: 'var(--kim)', x: 72, delay: 8,   duration: 22 },
      { char: '水', color: 'var(--thuy)',x: 88, delay: 3.5, duration: 26 },
    ];
    kanjis.forEach(k => {
      const el = document.createElement('div');
      el.className = 'kanji-float';
      el.textContent = k.char;
      el.style.cssText = `
        left: ${k.x}%;
        bottom: -80px;
        color: rgba(0,0,0,0.04);
        animation-duration: ${k.duration}s;
        animation-delay: -${k.delay}s;
      `;
      nguhanhSection.appendChild(el);
    });
  }


  // ─── 5. MAGNETIC BUTTONS ───
  if (!isMobile() && !prefersReduced) {
    document.querySelectorAll('.btn-primary, .btn-add-hanh, .nav-btn-cta').forEach(btn => {
      btn.classList.add('btn-magnetic');

      btn.addEventListener('mousemove', e => {
        const r = btn.getBoundingClientRect();
        const cx = r.left + r.width / 2;
        const cy = r.top  + r.height / 2;
        const dx = (e.clientX - cx) * 0.35;
        const dy = (e.clientY - cy) * 0.35;
        btn.style.transform = `translate(${dx}px, ${dy}px)`;
      });

      btn.addEventListener('mouseleave', () => {
        btn.style.transform = '';
      });
    });
  }


  // ─── 6. RIPPLE EFFECT — CART BUTTONS ───
  function addRipple(e) {
    const btn = e.currentTarget;
    btn.classList.add('ripple-container');
    const r = btn.getBoundingClientRect();
    const size = Math.max(r.width, r.height) * 2;
    const x = e.clientX - r.left - size / 2;
    const y = e.clientY - r.top  - size / 2;

    const wave = document.createElement('span');
    wave.className = 'ripple-wave';
    wave.style.cssText = `width:${size}px;height:${size}px;left:${x}px;top:${y}px`;
    btn.appendChild(wave);

    wave.addEventListener('animationend', () => wave.remove());

    // Bounce animation on button
    btn.classList.add('adding');
    btn.addEventListener('animationend', () => btn.classList.remove('adding'), { once: true });
  }

  document.querySelectorAll('.btn-add-cart, .btn-add-hanh').forEach(btn => {
    btn.addEventListener('click', addRipple);
  });


  // ─── 7. HANH TAB — SLIDING PILL ───
  const hanhTabs = document.querySelector('.hanh-tabs');
  if (hanhTabs) {
    const pill = document.createElement('div');
    pill.className = 'hanh-tab-pill';
    hanhTabs.prepend(pill);

    const hanhColors = {
      moc: '#456b4e', hoa: '#8B3A2A', tho: '#A07840', kim: '#7A6B5A', thuy: '#3D5C7A'
    };

    function updatePill(tab) {
      const r    = tab.getBoundingClientRect();
      const pr   = hanhTabs.getBoundingClientRect();
      pill.style.left  = (r.left - pr.left) + 'px';
      pill.style.width = r.width + 'px';
      const h = tab.dataset.h;
      if (h && hanhColors[h]) pill.style.background = hanhColors[h];
    }

    // Init
    const activeTab = hanhTabs.querySelector('.hanh-tab.active');
    if (activeTab) {
      pill.style.transition = 'none';
      updatePill(activeTab);
      requestAnimationFrame(() => { pill.style.transition = ''; });
    }

    const origSwitchHanh = window.switchHanh;
    window.switchHanh = function(h) {
      if (origSwitchHanh) origSwitchHanh(h);
      const tab = hanhTabs.querySelector(`.hanh-tab[data-h="${h}"]`);
      if (tab) updatePill(tab);
    };

    hanhTabs.querySelectorAll('.hanh-tab').forEach(tab => {
      tab.addEventListener('click', () => updatePill(tab));
    });
  }


  // ─── 8. COUNTER ANIMATION — PRICES ───
  function animateCounter(el, target, duration = 1200) {
    const start = performance.now();
    const formatted = target.toLocaleString('vi-VN');
    const suffix = el.querySelector('span') ? '' : '';

    function tick(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
      const val = Math.round(target * ease);
      // Only update the text node (first child), preserve child spans
      const textNode = Array.from(el.childNodes).find(n => n.nodeType === 3);
      if (textNode) textNode.textContent = val.toLocaleString('vi-VN');
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  const priceAmts = document.querySelectorAll('.price-amt');
  let countersDone = false;

  const counterObs = new IntersectionObserver(entries => {
    if (countersDone) return;
    entries.forEach(e => {
      if (e.isIntersecting) {
        countersDone = true;
        priceAmts.forEach(el => {
          const text = el.childNodes[0]?.textContent?.replace(/\./g, '').replace(/[^\d]/g, '');
          const num = parseInt(text, 10);
          if (!isNaN(num)) animateCounter(el, num);
        });
      }
    });
  }, { threshold: 0.5 });

  if (priceAmts.length > 0 && !prefersReduced) {
    counterObs.observe(priceAmts[0]);
  }


  // ─── 9. IMAGE 3D PARALLAX — INBOX VIEWER ───
  const inboxViewer = document.querySelector('.inbox-viewer');
  if (inboxViewer && !isMobile() && !prefersReduced) {
    const img = inboxViewer.querySelector('.inbox-viewer-img');
    inboxViewer.addEventListener('mousemove', e => {
      const r  = inboxViewer.getBoundingClientRect();
      const cx = r.width  / 2;
      const cy = r.height / 2;
      const dx = ((e.clientX - r.left) - cx) / cx;
      const dy = ((e.clientY - r.top)  - cy) / cy;
      if (img) img.style.transform = `scale(1.04) translate(${dx * -10}px, ${dy * -8}px)`;
    });
    inboxViewer.addEventListener('mouseleave', () => {
      if (img) img.style.transform = '';
    });
  }


  // ─── 10. MARQUEE SLOW ON HOVER ───
  const marqueeStrip = document.querySelector('.marquee-strip');
  if (marqueeStrip && !prefersReduced) {
    marqueeStrip.addEventListener('mouseenter', () => {
      document.querySelector('.marquee-track').style.animationPlayState = 'paused';
    });
    marqueeStrip.addEventListener('mouseleave', () => {
      document.querySelector('.marquee-track').style.animationPlayState = 'running';
    });
  }


  // ─── 11. TOAST NOTIFICATION ───
  window.showToast = function(msg, duration = 2800) {
    let toast = document.querySelector('.ng-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'ng-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toast._timer);
    toast._timer = setTimeout(() => toast.classList.remove('show'), duration);
  };

  // Hook toast into addToCart
  const origAddToCart = window.addToCart;
  window.addToCart = function(product) {
    if (origAddToCart) origAddToCart(product);
    window.showToast('✓ Đã thêm vào giỏ hàng');
  };


  // ─── 12. HERO EM GLOW (data-text mirror) ───
  const heroEm = document.querySelector('.hero-h1 em');
  if (heroEm) heroEm.setAttribute('data-text', heroEm.textContent);


  // ─── 13. STAGGER on parent containers ───
  document.querySelectorAll('.pricing-grid, .reviews-grid, .hanh-tabs, .ritual-timeline').forEach(el => {
    el.classList.add('stagger-parent');
  });


  // ─── 14. ENHANCED INTERSECTION OBSERVER (stagger reset) ───
  // Already handled by existing observer — just ensure stagger-parent children
  // get the right transition-delays applied.
  document.querySelectorAll('.stagger-parent > .fade-up').forEach((el, i) => {
    el.style.transitionDelay = (i * 0.08) + 's';
  });

})();
