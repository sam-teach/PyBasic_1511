"""
parser
"""
import requests
from bs4 import BeautifulSoup

url = 'https://auto.ria.com/uk/car/used/?page='


def get_html(link_page: str):
    """
    Getting html from link
    :param link_page:
    :return: html or status code(if not 200)
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    data = requests.get(link_page, headers=headers)
    if data.status_code == 200:
        return data.text
    else:
        return data.status_code


def get_links_from_page(page: str) -> list:
    """
    Create list with links from one page
    :param page:
    :return list:
    """
    clear_links = []
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a', class_='address')
    for link in links:
        clear_links.append(link.get('href'))
    return clear_links


def get_data_from_page(one_auto_link: str) -> dict:
    """
    Return dictionary with data from one auto
    url +
    name +
    price +
    year
    miles
    city
    transmission
    4*4
    engine
    fuel
    :param one_auto_link:
    :return dictionary:
    """

    soup = BeautifulSoup(get_html(one_auto_link), 'html.parser')
    result = {}
    result.update({'url': one_auto_link})
    result.update({'name': soup.find('h1').text})
    result.update({'price': soup.find('div', class_='price_value').find('strong').text})
    # print(soup.find('div', class_='price_value').find('strong').text)
    return result


page_text = get_html(url + '2')
links = get_links_from_page(page_text)
result = []
for link in links:
    result.append(get_data_from_page(link))
print(result)
# one = 'https://auto.ria.com/uk/auto_hyundai_santa_fe_33813770.html'
# get_data_from_page(one)
