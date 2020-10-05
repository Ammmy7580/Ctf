import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

url = 'http://chal.ctf.b01lers.com:3001'

token = #  <GET IT FROM THE /maze file <DO IT FAST>>  #
r = requests.post(url+'/mem', data = {'token' : token})

print(r.text)


