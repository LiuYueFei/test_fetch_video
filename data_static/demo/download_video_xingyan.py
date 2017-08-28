from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

html = urlopen("https://xingyan.panda.tv/7351608")
bsObj = BeautifulSoup(html, "lxml")
a = bsObj.find("script", text=re.compile(r".*roominfo"))
match_str = re.match(r"^.*?(\{.*\})", a.get_text())
# print(match_str)
my_str = match_str.group(1)
my_json = json.loads(my_str)
print(my_json)
