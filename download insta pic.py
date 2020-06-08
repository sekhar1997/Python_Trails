import requests
from bs4 import BeautifulSoup

username = "som_sekhar"
URL = "https://www.instagram.com/{}/"


def pic_downloader(username):
    r = requests.get(URL.format(username))
    s = BeautifulSoup(r.text, "html.parser")
    p = s.find("meta", property="og:image").attrs['content']

    with open(username+'.jpg', "wb")as pic:
        binary = requests.get(p).content
        pic.write(binary)


if __name__ == "__main__":
    username = "som_sekhar"
    pic_downloader(username)
