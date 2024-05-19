from bs4 import BeautifulSoup
import requests


def pars():
    count = 0
    description = {'Name': [], 'Writer': [], 'Price': []}
    url = 'https://www.chitai-gorod.ru/search?phrase=python&page={}'

    while True:
        count += 1
        response = requests.get(url.format(count))
        print(response.status_code)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all('article')

        for article in articles:
            name = article.find('div', class_='product-title__head').get_text(strip=True)
            writer = article.find('div', class_='product-title__author').get_text(strip=True)
            price_element = article.find('div', class_='product-price__value product-price__value--discount')

            if price_element:
                price = price_element.get_text(strip=True)
            else:
                price = "no price"

            description['Name'].append(name)
            description['Writer'].append(writer)
            description['Price'].append(price)

    return description