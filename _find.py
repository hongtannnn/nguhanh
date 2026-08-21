with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

body_pos = content.find('<body>')
ci_pos = content.find('id="checkin"')
nh_pos = content.find('id="nguhanh"')
script_end = content.rfind('</script>')
print('body at:', body_pos)
print('checkin at:', ci_pos)
print('nguhanh at:', nh_pos)
print('last script end at:', script_end)
print('around script end:', repr(content[script_end-60:script_end+15]))
