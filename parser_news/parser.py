import requests
from bs4 import BeautifulSoup

site = 'https://strana.ua/news'


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    domen = 'https://strana.ua'
    soup = BeautifulSoup(html, 'lxml')

    titles = soup.find('div', {'class': 'lenta'}).find_all(
                                                      'div',
                                                      {'class': 'title'}
    )

    links = []

    for div in titles:
        a = div.find('a', {'class': 'article'}).get('href')
        link = domen + a
        links.append(link)

    return links


def get_links_data(html):
    soup = BeautifulSoup(html, 'lxml')

    title = soup.find('h1', {'class': 'article'}).text.strip()
    object_news = soup.find('div', id='article-text').find_all('p')
    news = []
    for p in object_news:
        news.append(p.text)
    return title, news


def write_news(tuple):
    name = 'News for OLEGA.doc'

    with open(name, 'a') as f:
        f.write(tuple[0])
        f.write('\n')
        for el in tuple[1]:
            f.write(el)
        f.write('\n\n\n')


def main():
    all_links = get_all_links(get_html(site))

    for link in all_links:
        write_news(get_links_data(get_html(link)))


if __name__ == '__main__':
    main()
