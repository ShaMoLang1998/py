import requests
from bs4 import BeautifulSoup

url = 'https://bj.lianjia.com/ershoufang/pg2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
resp = requests.get(url, headers=headers)

html = resp.text

soup = BeautifulSoup(html, 'html.parser')
# print(soup)
infos = soup.find('ul', {'class': 'sellListContent'}).find_all('li')
# print(infos)

for info in infos:
    name = info.find('div', {'class': 'title'}).find('a').get_text()
    print(name)
    price = info.find('div', {'class': 'priceInfo'}).find('div', {'class': 'totalPrice'}).find('span').get_text()
    print(price)
    address = info.find('div', {'class': 'address'}).find('div', {'class': 'houseInfo'}).get_text()
    print(address)
    with open(r'C:\Users\Think\PycharmProjects\WenZhangProject\lianjia\lianjia.csv', 'a', encoding='utf-8') as f:
        f.write("{},{},{}\n".format(name,price,address))