import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen("https://www.google.com")
except urllib.error.URLError:
    print("Ocorreu um erro!")
else:
    print("Tudo certo!")