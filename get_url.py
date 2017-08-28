from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

base_url = "https://baike.baidu.com"
init_item = "/item/zookeeper"

html = urlopen(base_url + init_item)
bsObj = BeautifulSoup(html, "lxml")

# 获得所有外链
out_url_list = bsObj.findAll("a", {"href": re.compile(r"^(http://|https://|www\.)")})
for out_url in out_url_list:
    print("%s-->%s" % (out_url.get_text().strip(), out_url.attrs["href"].strip()))
# 获取所有內链
inner_url_list = bsObj.findAll("a", {"href": re.compile(r"^/item/")})
for inner_url in inner_url_list:
    print("%s-->%s" % (inner_url.get_text().strip(), inner_url.attrs["href"].strip()))
