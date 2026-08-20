import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'photos/1.jpg': 'photos/logo.jpg', 
    'photos/5.jpg': 'photos/moc.jpg',
    'photos/3.jpg': 'photos/hoa.jpg',
    'photos/7.jpg': 'photos/tho.jpg',
    'photos/4.jpg': 'photos/kim.jpg',
    'photos/6.jpg': 'photos/thuy.jpg',
    'photos/9.jpg': 'photos/aroma.jpg',
    'photos/10.jpg': 'photos/journal.jpg',
    'photos/11.jpg': 'photos/qr.jpg'
}
for old, new in replacements.items():
    content = content.replace(old, new)

content = content.replace('"photos/8.jpg" alt="Journal"', '"photos/journal.jpg" alt="Journal"')
content = content.replace('data-img="photos/8.jpg" data-title="Playlist', 'data-img="photos/playlist.jpg" data-title="Playlist')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
