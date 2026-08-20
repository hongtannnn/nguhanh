import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_html = r'''<!-- NGHI THỨC -->
<section id="nghithuc">
  <div class="ritual-bg-dots"></div>
  <div class="container">
    <div class="ritual-hdr fade-up">
      <div class="section-tag">Nghi thức</div>
      <h2>15 phút. 6 bước.<br><em>Một hành trình thống nhất.</em></h2>
      <p>Không phải checklist, không phải nhiệm vụ. Đây là một chuỗi trải nghiệm được thiết kế để đưa bạn từ trạng thái bồn chồn về lại với chính mình.</p>
    </div>
    <div class="ritual-grid">
      <div class="ritual-card fade-up"><span class="r-num">01</span><div class="r-icon">🪷</div><div class="r-time">Phút 1–2</div><h3 class="r-title">Check-in</h3><p class="r-desc">Quét QR, trả lời 3 câu hỏi ngắn. Hệ thống gợi ý dòng trà Ngũ Hành phù hợp nhất với trạng thái cảm xúc hôm nay của bạn.</p></div>
      <div class="ritual-card fade-up" style="transition-delay:.08s"><span class="r-num">02</span><div class="r-icon">🍵</div><div class="r-time">Phút 2–7</div><h3 class="r-title">Brew & Disconnect</h3><p class="r-desc">Pha trà, đặt điện thoại xuống. Theo dõi nước sôi, mùi thảo mộc lan tỏa — tín hiệu để cơ thể biết: đã đến giờ nghỉ ngơi.</p></div>
      <div class="ritual-card fade-up" style="transition-delay:.16s"><span class="r-num">03</span><div class="r-icon">🌿</div><div class="r-time">Phút 7–10</div><h3 class="r-title">Aroma & Vibe</h3><p class="r-desc">Xịt Aroma Spray, bật playlist. Kết hợp khứu giác và thính giác để tạo không gian thư giãn toàn diện, ngắt hẳn khỏi dòng thông tin.</p></div>
      <div class="ritual-card fade-up" style="transition-delay:.08s"><span class="r-num">04</span><div class="r-icon">✍️</div><div class="r-time">Phút 10–14</div><h3 class="r-title">Journal</h3><p class="r-desc">Mở Emotional Journal, viết theo prompts theo Hành của ngày. Không cần văn hay — chỉ cần thành thật với chính mình vài dòng thôi.</p></div>
      <div class="ritual-card fade-up" style="transition-delay:.16s"><span class="r-num">05</span><div class="r-icon">🔮</div><div class="r-time">Phút 14–15</div><h3 class="r-title">Reflect</h3><p class="r-desc">Đọc lại những gì vừa viết. Nhận ra điều bạn đang thực sự cảm thấy. Một câu hỏi nhỏ kết thúc nghi thức: "Mình cần gì nhất lúc này?"</p></div>
      <div class="ritual-card fade-up" style="transition-delay:.24s"><span class="r-num">06</span><div class="r-icon">🌱</div><div class="r-time">Mỗi ngày</div><h3 class="r-title">Duy trì</h3><p class="r-desc">21 ngày để hình thành thói quen. Mỗi ngày một Hành khác nhau — tùy cảm xúc. Không cứng nhắc, không áp lực, không "phải làm".</p></div>
    </div>
  </div>
</section>'''

new_html = r'''<!-- NGHI THỨC -->
<section id="nghithuc" class="ritual-light">
  <div class="container">
    <div class="ritual-hdr fade-up">
      <div class="section-tag-line"><span>NGHI THỨC 15 PHÚT</span></div>
      <h2 style="color:var(--green-dark)">15 phút. 6 bước.<br><em>Một hành trình thống nhất.</em></h2>
      <p style="color:#7a6a5a">Không cần app phức tạp, không cần huấn luyện. Chỉ cần chiếc hộp và 15 phút chọn cho chính mình.</p>
    </div>
    
    <div class="ritual-timeline">
      <div class="rt-line"></div>
      
      <!-- Step 01 -->
      <div class="rt-step">
        <div class="rt-img-side fade-up">
          <div class="rt-img-wrapper">
            <img src="photos/qr.jpg" alt="Check-in">
            <div class="rt-img-tag"><span class="rt-tag-label">CHECK-IN</span><span class="rt-tag-time"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><path d="M12 6v6l4 2" stroke-width="2"/></svg> 2 phút</span></div>
          </div>
        </div>
        <div class="rt-dot"><span></span></div>
        <div class="rt-text-side fade-up" style="transition-delay:.1s">
          <div class="rt-num">01</div>
          <h3 class="rt-title"><div class="rt-icon">🪷</div> Quét QR · Gọi tên cảm xúc</h3>
          <p class="rt-desc">Trả lời 3 câu hỏi ngắn để hệ thống hiểu bạn đang "thiếu" Hành nào hôm nay. Không phải trắc nghiệm tâm lý, chỉ là một khoảnh khắc dừng lại.</p>
        </div>
      </div>
      
      <!-- Step 02 -->
      <div class="rt-step right">
        <div class="rt-text-side fade-up">
          <div class="rt-num">02</div>
          <h3 class="rt-title"><div class="rt-icon">🍵</div> Pha trà · Ngắt kết nối</h3>
          <p class="rt-desc">Đặt xuống chiếc laptop. Rót nước sôi. Theo dõi nước chuyển màu, mùi thảo mộc lan tỏa — tín hiệu để cơ thể biết: đã đến giờ nghỉ ngơi.</p>
        </div>
        <div class="rt-dot"><span></span></div>
        <div class="rt-img-side fade-up" style="transition-delay:.1s">
          <div class="rt-img-wrapper">
            <img src="photos/8.jpg" alt="Pha trà">
            <div class="rt-img-tag"><span class="rt-tag-label">BREW</span><span class="rt-tag-time"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><path d="M12 6v6l4 2" stroke-width="2"/></svg> 5 phút</span></div>
          </div>
        </div>
      </div>
      
      <!-- Step 03 -->
      <div class="rt-step">
        <div class="rt-img-side fade-up">
          <div class="rt-img-wrapper">
            <img src="photos/playlist.jpg" alt="Nghe nhạc">
            <div class="rt-img-tag"><span class="rt-tag-label">VIBE</span><span class="rt-tag-time"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><path d="M12 6v6l4 2" stroke-width="2"/></svg> 1 phút</span></div>
          </div>
        </div>
        <div class="rt-dot"><span></span></div>
        <div class="rt-text-side fade-up" style="transition-delay:.1s">
          <div class="rt-num">03</div>
          <h3 class="rt-title"><div class="rt-icon">🎵</div> Nghe nhạc · Chạm tần số</h3>
          <p class="rt-desc">Trang web tự động phát playlist thư giãn tương ứng cảm xúc: lo-fi, piano, âm thanh thiên nhiên hoặc âm nhạc tần số 432Hz — dịu dàng đưa bạn vào trạng thái flow.</p>
        </div>
      </div>
      
      <!-- Step 04 -->
      <div class="rt-step right">
        <div class="rt-text-side fade-up">
          <div class="rt-num">04</div>
          <h3 class="rt-title"><div class="rt-icon">🌿</div> Xịt phòng · Khứu giác</h3>
          <p class="rt-desc">Xịt một hơi Aroma Spray ra không gian. Chỉ trong vài giây, mùi hương sẽ làm dịu hệ thần kinh và kết nối bạn sâu hơn với thực tại.</p>
        </div>
        <div class="rt-dot"><span></span></div>
        <div class="rt-img-side fade-up" style="transition-delay:.1s">
          <div class="rt-img-wrapper">
            <img src="photos/aroma.jpg" alt="Aroma Spray">
            <div class="rt-img-tag"><span class="rt-tag-label">AROMA</span><span class="rt-tag-time"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><path d="M12 6v6l4 2" stroke-width="2"/></svg> 1 phút</span></div>
          </div>
        </div>
      </div>
      
      <!-- Step 05 -->
      <div class="rt-step">
        <div class="rt-img-side fade-up">
          <div class="rt-img-wrapper">
            <img src="photos/journal.jpg" alt="Viết Journal">
            <div class="rt-img-tag"><span class="rt-tag-label">REFLECT</span><span class="rt-tag-time"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><path d="M12 6v6l4 2" stroke-width="2"/></svg> 6 phút</span></div>
          </div>
        </div>
        <div class="rt-dot"><span></span></div>
        <div class="rt-text-side fade-up" style="transition-delay:.1s">
          <div class="rt-num">05</div>
          <h3 class="rt-title"><div class="rt-icon">✍️</div> Viết journal · Giải tỏa</h3>
          <p class="rt-desc">1–2 prompts gợi mở giúp bạn đưa những dòng suy nghĩ hỗn loạn xuống giấy. Không cần văn hay, chỉ cần thật. Đó là khoảnh khắc bạn thực sự lắng nghe mình.</p>
        </div>
      </div>
      
      <!-- Step 06 -->
      <div class="rt-step right">
        <div class="rt-text-side fade-up">
          <div class="rt-num">06</div>
          <h3 class="rt-title"><div class="rt-icon">🌱</div> Duy trì · Hình thành thói quen</h3>
          <p class="rt-desc">21 ngày để hình thành thói quen. Mỗi ngày một Hành khác nhau — tùy cảm xúc. Không cứng nhắc, không áp lực, không "phải làm".</p>
        </div>
        <div class="rt-dot"><span></span></div>
        <div class="rt-img-side fade-up" style="transition-delay:.1s">
          <div class="rt-img-wrapper">
            <img src="photos/11.jpg" alt="Duy trì">
            <div class="rt-img-tag"><span class="rt-tag-label">ROUTINE</span><span class="rt-tag-time"><svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke-width="2"/><path d="M12 6v6l4 2" stroke-width="2"/></svg> Mỗi ngày</span></div>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</section>'''

if old_html in content:
    content = content.replace(old_html, new_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Could not find old_html to replace")
