import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

pageLinks = set()
pageLinks.add("/item/zookeeper")
i = 0


def getLinks(articleUrl):
    global pageLinks
    global i
    i = i + 1
    html = urlopen("https://baike.baidu.com" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    main_content = bsObj.find("div", {"class": "main-content"})

    for a_link in main_content.findAll("a", {"href": re.compile(r"^/item/[a-zA-Z0-9_/%\.\?\=\&-]+$")}):
        if a_link.attrs["href"] not in pageLinks:
            pageLinks.add(a_link.attrs["href"])
            print("%s -->%s" % (a_link.get_text(), a_link.attrs["href"].strip()))

    getLinks(pageLinks.pop())


# print(pageLinks)
getLinks(pageLinks.pop())
