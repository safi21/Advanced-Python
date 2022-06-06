import html
import re
import requests
import json
import os
import sys


# returns contents of a url.
def download_content(url):
    r = requests.get(url)
    contents = r.text
    return html.unescape(contents)


def extract_links(contents):
    url_pattern = re.compile('<h3>.*?<a href="(.*?)"')
    results = re.findall(url_pattern, contents)
    links= ["https://books.toscrape.com/"+item for item in results]
    return links
    

#get name of the book
def get_book_name(content):
    book_name_pattern = re.compile('<h1>"*(.*?)"*</h1>')
    book_name = re.findall(book_name_pattern, content)
    return book_name[0]


#img src
def get_img(content):
    img_pattern = re.compile('<img src="(.*?)"')
    img = re.findall(img_pattern, content)
    return "https://books.toscrape.com/" + img[0]#[6:]


#price
def get_price(content):
    price_pattern = re.compile('<p class="price_color">(.*?)</p>')
    price = re.findall(price_pattern,content)
    return price[0][2:]


#upc
def get_upc(content):
    upc_pattern = re.compile('<th>UPC</th>.*?<td>(.*?)</td>')
    upc = re.findall(upc_pattern, content)
    return upc[0]


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
        json.dump(filedata, f, indent=4, ensure_ascii=False)


def scrap():
    base_url = 'https://books.toscrape.com/catalogue/'
    urls = [f"{base_url}page-{i}.html" for i in range(2, 51)]

    for url in urls:
        content = download_content(url)
        links = extract_links(content)
        # to check if the code is running properly.
        print(url)

        for link in links:
            page_content = download_content(link)

            name = get_book_name(page_content)
            img = get_img(page_content)
            price = get_price(page_content)
            upc = get_upc(page_content)

            data = {'Name': name, 'Price (Pounds)': price, 'UPC': upc, 'Cover': img}

            save_to_file(data=data)


if __name__ == "__main__":
    scrap()