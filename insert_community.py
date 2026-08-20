import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_section = r'''
<!-- GÓC BÌNH YÊN -->
<section id="congdong">
  <div class="container">
    <div class="congdong-hdr fade-up">
      <div class="section-tag" style="justify-content:center">Góc Bình Yên</div>
      <h2>Những dòng suy nghĩ được để lại<br><em>sau 15 phút.</em></h2>
      <p>Không phán xét, không danh tính, chỉ có sự sẻ chia.</p>
      <button class="btn-primary" style="margin-top:24px" onclick="openCongDongModal()">Chia sẻ ẩn danh <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg></button>
    </div>
    
    <div class="congdong-masonry fade-up" style="transition-delay:.1s">
      <div class="cd-col">
        <div class="cd-card">
          <div class="cd-tag"><span class="c-dot" style="background:var(--moc)"></span>Mộc · Calm</div>
          <p class="cd-text">"Hôm nay chạy deadline mệt nhoài. Chỉ một mùi hương thảo mộc cũng đủ kéo mình lại thực tại."</p>
          <div class="cd-author">Người lạ từ Sài Gòn</div>
        </div>
        <div class="cd-card">
          <div class="cd-tag"><span class="c-dot" style="background:var(--hoa)"></span>Hỏa · Release</div>
          <p class="cd-text">"Mình đã khóc khi viết vào journal. Rất nhiều ấm ức không thể nói ra cùng ai. Cảm ơn vì 15 phút này."</p>
          <div class="cd-author">Một buổi tối mưa</div>
        </div>
      </div>
      
      <div class="cd-col" style="margin-top:40px">
        <div class="cd-card">
          <div class="cd-tag"><span class="c-dot" style="background:var(--tho)"></span>Thổ · Balance</div>
          <p class="cd-text">"Cảm giác cầm tách trà nóng trên tay thật an tâm. Giống như có ai đó đang ôm lấy mình vậy."</p>
          <div class="cd-author">Ngọc, 28 tuổi</div>
        </div>
        <div class="cd-card">
          <div class="cd-tag"><span class="c-dot" style="background:var(--kim)"></span>Kim · Comfort</div>
          <p class="cd-text">"Chưa bao giờ mình tắt điện thoại suốt 15 phút mà không thấy bồn chồn. Thật kỳ diệu."</p>
          <div class="cd-author">Freelancer hay overthinking</div>
        </div>
      </div>
      
      <div class="cd-col">
        <div class="cd-card">
          <div class="cd-tag"><span class="c-dot" style="background:var(--thuy)"></span>Thủy · Restore</div>
          <p class="cd-text">"Nghe bản nhạc 432Hz tự nhiên mọi gánh nặng bay đi đâu mất. Yên bình đến lạ."</p>
          <div class="cd-author">Chàng trai thích màu xanh</div>
        </div>
        <div class="cd-card">
          <div class="cd-tag"><span class="c-dot" style="background:var(--moc)"></span>Mộc · Calm</div>
          <p class="cd-text">"Tôi nhận ra mình đã bỏ bê bản thân quá lâu. Bắt đầu từ hôm nay, 15 phút này là bất khả xâm phạm."</p>
          <div class="cd-author">Người bắt đầu yêu mình</div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

modal_html = r'''
<!-- CỘNG ĐỒNG MODAL -->
<div class="modal-overlay" id="cdModal" onclick="closeCongDongModal()">
  <div class="modal-content cd-modal" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeCongDongModal()"><svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg></button>
    <div class="auth-hdr">
      <h3>Gửi gắm nỗi niềm</h3>
      <p>Chia sẻ một điều bạn cảm thấy sau nghi thức hôm nay. Hoàn toàn ẩn danh.</p>
    </div>
    <form class="auth-form" onsubmit="submitCongDong(event)">
      <div class="form-group">
        <label class="form-label">Bạn vừa trải nghiệm Hành nào?</label>
        <select class="form-input" id="cd-hanh" required style="appearance:auto">
          <option value="moc">Mộc · Calm</option>
          <option value="hoa">Hỏa · Release</option>
          <option value="tho">Thổ · Balance</option>
          <option value="kim">Kim · Comfort</option>
          <option value="thuy">Thủy · Restore</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Dòng suy nghĩ (Tối đa 150 ký tự)</label>
        <textarea class="form-input" id="cd-text" rows="3" maxlength="150" required placeholder="Hôm nay mình thấy..."></textarea>
      </div>
      <div class="form-group">
        <label class="form-label">Ký tên (Ẩn danh)</label>
        <input type="text" class="form-input" id="cd-author" required placeholder="Ví dụ: Kẻ mộng mơ, Hà Nội ngày mưa...">
      </div>
      <button type="submit" class="btn-primary" style="width:100%;margin-top:10px">Gửi thông điệp vào gió</button>
    </form>
    <div id="cd-success" style="display:none;text-align:center;padding:20px 0;color:var(--green-dark);">
      <div style="font-size:32px;margin-bottom:12px">✨</div>
      <h4 style="font-size:18px;margin-bottom:8px">Đã gửi thành công</h4>
      <p style="font-size:14px;color:#7a6a5a">Cảm ơn bạn đã sẻ chia. Thông điệp của bạn đang sưởi ấm những người khác.</p>
      <button class="btn-outline" style="margin-top:20px" onclick="closeCongDongModal()">Đóng</button>
    </div>
  </div>
</div>
'''

# Insert the community section after </section> of testimonials
for i, line in enumerate(lines):
    if '<section id="banggia">' in line:
        lines.insert(i, new_section + "\n")
        break

# Insert the modal before </body>
for i, line in enumerate(lines):
    if '</body>' in line:
        lines.insert(i, modal_html + "\n")
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
