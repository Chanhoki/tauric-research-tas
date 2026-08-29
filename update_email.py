import codecs

with codecs.open('C:/tauric-research-tas/privacy.html', 'r', 'utf-8') as f:
    html = f.read()

html = html.replace('admin@tauric-research.com', 'tm.admin26@gmail.com')

with codecs.open('C:/tauric-research-tas/privacy.html', 'w', 'utf-8') as f:
    f.write(html)
print("Updated email in C:/tauric-research-tas/privacy.html!")
