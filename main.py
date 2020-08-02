import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
def save_xl():
    #Функция, которая сохраняет работу парсера в .xls формат
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test sheet')
    row = 0
    while row < len(item):
        for i in item:
            ws.write(row, 0, f'{i["brand"]}' )
            ws.write(row, 1, f'{i["prise"]}')
            ws.write(row, 2, f'{i["link"]}' )
            row += 1
    wb.save('main.xls')#ваш файлик
def parse():
    #Стандартый набросок парсинга
    global item
    URL = 'https://www.wildberries.ru/catalog/obuv/muzhskaya/kedy-i-krossovki?sort=priceup'
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
               'accept': '*/*'}

    html = requests.get(URL, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    items = soup.findAll('div', class_='dtList-inner')
    item = []
    #Перебираю значения
    for i in items:
        item.append({
            'brand': i.find('div', class_='dtlist-inner-brand-name').get_text(),
            'prise': i.find('ins', class_='lower-price').get_text(),
            'link': i.find('a', class_='ref_goods_n_p j-open-full-product-card').get('href')
        })
    global item_all

    for item_all in item:
        print(f'{item_all["brand"]}{item_all["prise"]},{item_all["link"]}...\n')
        save_xl()
if __name__ == '__main__':
    parse()