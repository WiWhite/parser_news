import requests
from bs4 import BeautifulSoup

site = 'https://strana.ua/news'


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    domen = 'https://strana.ua'
    soup = BeautifulSoup(html, 'lxml')

    titles = soup.find('div', {'class': 'lenta'}).find_all('div', {'class': 'title'})

    links = []

    for div in titles:
        a = div.find('a', {'class': 'article'}).get('href')
        link = domen + a
        links.append(link)

    return links

def main():
    all_links = get_all_links(get_html(site))

    for link in all_links:
        print(link)


if __name__ == '__main__':
    main()
