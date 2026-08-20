css_content = r'''
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
