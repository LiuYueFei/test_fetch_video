from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://baike.baidu.com/item/zookeeper")
bsObj = BeautifulSoup(html, "lxml")
main_content = bsObj.find("div", {"class": "main-content"})
aList = main_content.findAll("a", {"href": re.compile(r"^/item/[a-zA-Z0-9_/%\.\?\=\&-]+$")})
for a in aList:
    print("%s -->%s" % (a["href"], a.get_text()))
summary = main_content.find("div", {"class": "lemma-summary"}).get_text()
print("Summary:\n %s" % (summary))
contentList = main_content.findAll("div", {"class": "para"})
for content in contentList:
    print(content.get_text(), end="")
