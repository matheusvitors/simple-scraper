from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try: 
    html = urlopen("https://www.python.org/")
except HTTPError as e: 
    print(e)
except URLError: 
    print("Endereço não encontrado ou servidor fora do ar")
else: 
    res = BeautifulSoup(html.read(), "html.parser")

    if res.title is None: 
        print("Tag not found!")
    else: 
        print(res.title)