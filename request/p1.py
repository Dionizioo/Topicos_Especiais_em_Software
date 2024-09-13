import requests
from bs4 import BeautifulSoup

q = "dolar"
rep = requests.get(f"https://www.uol.com.br")

#print(rep.text)# tudo que está dentro do site

site = BeautifulSoup(rep.text, "html.parser")

res = site.find('article')
#print(res.prettify())

titulo = res.find('h3')
tag_a = res.find('a')
#print(titulo.text)
#print(tag_a['href'])