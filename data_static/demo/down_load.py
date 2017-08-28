from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

html = urlopen("https://www.panda.tv/537239")
bsObj = BeautifulSoup(html, "lxml",from_encoding="utf-8")
#script_str = bsObj.find("script", text=re.compile(r".*roominfo")).get_text().replace(";","").replace("window._config_roominfo = ","").replace("'","\"")
print(bsObj)

#print(json.loads(script_str))
# #match_str = re.match(r".*?(\{.*\})",script_str)
# #print(match_str)
# #my_str = match_str.group(1)
# #my_json = json.loads(my_str)
# #print(my_json)
