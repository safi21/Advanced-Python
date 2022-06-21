import re
import requests
import json
import os
import sys

#returns web content of a given url.
def get_content(url):
    r = requests.get(url)
    content = r.text
    return content

#returns list of book urls of a given page
def book_url(content):
    url_pattern = re.compile('<h3>.*?<a href="(.*?)"')
    links = re.findall(url_pattern, content)
    return ['https://books.toscrape.com/catalogue/'+link for link in links]

#same as previous just for first page
def book_url1(content):
    url_pattern = re.compile('<h3>.*?<a href="(.*?)"')
    links = re.findall(url_pattern, content)
    return ['https://books.toscrape.com/'+link for link in links]

#returns name of the book
def get_book_name(content):
    url_pattern = re.compile('<h1>(.*?)<')
    book_name = re.findall(url_pattern, content)
    return book_name[0]

#returns price of the book
def get_price(content):
    price_pattern = re.compile('<p class="price_color">(.*?)</p>')
    price = re.findall(price_pattern,content)
    return price[0][2:]

#returns upc of the book
def get_upc(content):
    upc_pattern = re.compile('<th>UPC</th>.*?<td>(.*?)</td>')
    upc = re.findall(upc_pattern, content)
    return upc[0]

#returns image of the book
def get_img(content):
    img_pattern = re.compile('<img src="(.*?)"')
    img = re.findall(img_pattern, content)
    return 'https://books.toscrape.com/'+img[0][6:]

#skeleton for saving all data as in json format
def write_skeleton(filename):
    skel = """{
        
    "Book Details": [
        
    ]
}
    """

    if not os.path.exists(filename):
        try:
            with open(filename, 'w') as f:
                f.write(skel)
        except Exception as e:
            print('Could not open file')
            sys.exit(1)


def save_to_file(filename='data.json', data=''):
    if filename[-5:] != '.json':
        filename += '.json'

    write_skeleton(filename)

    with open(filename, 'r+') as f:
        filedata = json.load(f)
        filedata["Book Details"].append(data)
        f.seek(0)
        json.dump(filedata, f, indent=4)#, ensure_ascii=False)

#returns the link of next page
def next_page(content):
    url_pattern = re.compile('<li class="next".*?"(.*?)"')
    next_page = re.findall(url_pattern,content)
    if len(next_page) != 0:
        if 'catalogue' not in next_page[0]:
            return 'https://books.toscrape.com/catalogue/'+next_page[0]
        else:
            return 'https://books.toscrape.com/'+next_page[0]
    else:
        exit(1)


def scrap():
    url = "https://books.toscrape.com/"
    contents = get_content(url)
    links1 = book_url1(contents)
    for link in links1:
        page_content = get_content(link)
        name = get_book_name(page_content)
        img = get_img(page_content)
        price = get_price(page_content)
        upc = get_upc(page_content)
        data = {'Name': name, 'Price (Pounds)': price, 'UPC': upc, 'Cover': img}
        save_to_file(data=data)
    url = 'https://books.toscrape.com/catalogue/page-2.html'
    while True:
        contents = get_content(url)
        links = book_url(contents)
        for link in links:
            page_content = get_content(link)
            name = get_book_name(page_content)
            print(name)
            img = get_img(page_content)
            price = get_price(page_content)
            upc = get_upc(page_content)
            data = {'Name': name, 'Price (Pounds)': price, 'UPC': upc, 'Cover': img}
            save_to_file(data=data)
        url = next_page(contents)

if __name__ == "__main__":
    scrap()