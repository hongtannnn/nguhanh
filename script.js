
/* ─── CỘNG ĐỒNG ─── */
function openCongDongModal() {
  const modal = document.getElementById('cdModal');
  if (modal) {
    modal.classList.add('show');
    document.querySelector('.auth-form').style.display = 'block';
    document.getElementById('cd-success').style.display = 'none';
  }
}
function closeCongDongModal() {
  const modal = document.getElementById('cdModal');
  if (modal) {
    modal.classList.remove('show');
    setTimeout(() => {
        document.getElementById('cd-text').value = '';
        document.getElementById('cd-author').value = '';
    }, 300);
  }
}
function submitCongDong(e) {
  e.preventDefault();
  
  // Get values
  const hanhSelect = document.getElementById('cd-hanh');
  const hanhVal = hanhSelect.value;
  const hanhText = hanhSelect.options[hanhSelect.selectedIndex].text;
  const textVal = document.getElementById('cd-text').value;
  const authorVal = document.getElementById('cd-author').value;
  
  // Map value to CSS var for dot color
  const colorVar = `var(--${hanhVal})`;
  
  // Create card element
  const newCard = document.createElement('div');
  newCard.className = 'cd-card';
  newCard.innerHTML = `
    <div class="cd-tag"><span class="c-dot" style="background:${colorVar}"></span>${hanhText}</div>
    <p class="cd-text">"${textVal}"</p>
    <div class="cd-author">${authorVal}</div>
  `;
  
  // Add animation to the new card
  newCard.style.animation = 'fadeInUp 0.6s ease forwards';
  
  // Prepend to the first column
  const firstCol = document.querySelector('.congdong-masonry .cd-col');
  if (firstCol) {
    firstCol.insertBefore(newCard, firstCol.firstChild);
  }
  
  // Show success state
  document.querySelector('.auth-form').style.display = 'none';
  document.getElementById('cd-success').style.display = 'block';
}
