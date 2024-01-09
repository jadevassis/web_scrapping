import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    # Titulo
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    # print(titulo.text)
    # print(titulo['href']) # link da noiticia

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-centered subtitle">'})

    if subtitulo:
        print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtitulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)

# print(news)
