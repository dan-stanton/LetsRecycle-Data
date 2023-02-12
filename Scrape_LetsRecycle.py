import requests
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen
savepath = '/media/sf_Shared_Folder/'
urls = [
    'https://www.letsrecycle.com/prices/metals/ferrous-metal-prices/ferrous-scrap-metal-prices-2023',
    'https://www.letsrecycle.com/prices/metals/non-ferrous-metal-prices/non-ferrous-metal-prices-2023',
    'https://www.letsrecycle.com/prices/metals/aluminium-cans/aluminium-can-prices-2023/',
    'https://www.letsrecycle.com/prices/metals/steel-cans/steel-can-prices-2023/',
    'https://www.letsrecycle.com/prices/glass/glass-prices-2023/',
    'https://www.letsrecycle.com/prices/wood/wood-prices-2023/',
    'https://www.letsrecycle.com/prices/plastics/plastic-bottles/plastic-bottles-2023/',
    'https://www.letsrecycle.com/prices/plastics/plastic-film/plastic-film-2023/',
    'https://www.letsrecycle.com/prices/waste-paper/uk-domestic-mill-prices/2023-domestic-mill-prices/'
]

filetitle = [
    'Ferrous Prices',
    'Non-Ferrous Prices',
    'Aluminium Cans',
    'Steel Cans',
    'Glass',
    'Wood',
    'Plastic Bottles',
    'Plastic Film',
    'Domestic Mill'
]

for xcount, scrape in enumerate(urls):
    table_title = filetitle[xcount]
    req = Request(
        url=scrape, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    scrape_table = soup.find('table', class_ = 'table table-striped price-graph-table')

    table_months = []
    table_products = []
    table_prices = []
    count = 0
    for x in scrape_table.find_all('th'):
        if count > 0 and count < 13:
            table_months.append(x.text.strip())
        if count >= 13:
            table_products.append(x.text.strip())
        count += 1

    count = 1
    tmptable = []
    for x in scrape_table.find_all('td'):
        tmptable.append(x.text.strip())
        if count % 12 == 0:
            table_prices = table_prices + tmptable
            tmptable.clear()
        count += 1

    monthcount = 0
    productcountprice = 0
    with open(savepath + table_title + '.txt', 'w') as txt:
        for product in table_products:
            for month in table_months:
                if not table_prices[productcountprice] == '-':
                    txt.writelines(f'\n{product} - {month} Price: {table_prices[productcountprice]}\n')
                productcountprice += 1
            txt.writelines("========================================================")
            monthcount += 1
    


