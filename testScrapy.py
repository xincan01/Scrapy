from urllib.request import urlopen

html = urlopen('https://www.sohu.com/na/409703839_162758').read().decode('utf-8')

print(html)