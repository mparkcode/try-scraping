from bs4 import BeautifulSoup
import requests

base_url='https://www.consolemad.co.uk/product-category/microsoft/xbox/xbox-hardware/'
url = base_url

while url:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    
    pages=[]
    for ul in soup.find_all('ul', {'class': 'page-numbers'}):
        for li in ul.find_all('li'):
            for page_num in li.contents:
                if page_num.text == '←' or page_num.text == '→':
                    continue
                else:
                    pages.append(page_num.text)
    
    if soup.find('span', class_="current"):
        current_page = soup.find('span', class_="current").text
    else:
        current_page = None
    
    
    for product in soup.find_all('div', class_="entry-product"):
        
        picture_link = product.find('div', class_="entry-featured").a.img['src']
        print(picture_link)
        
        title = product.find('div', class_="entry-wrap").header.h3.a.text
        print(title)
        
        price = product.find('div', class_="entry-wrap").header.span.span.text
        print(price)
        
        print("--------------------------------")
    
        
    if current_page and current_page != pages[-1]:
        next_page = int(current_page) + 1
        url = base_url + "page/{}/".format(next_page)
    else:
        url = None
    
   