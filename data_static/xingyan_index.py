from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def getRoomInfo(roomid):
    html = urlopen("https://room.api.m.panda.tv/index.php?method=room.shareapi&roomid=" + roomid)
    json_data = json.loads(html.read().decode("utf-8"))["data"]
    print(json_data)
    print(json_data["hostinfo"])
    print(json_data["roominfo"]["pictures"])
    print(json_data["videoinfo"])


def getIndexPerson():
    html = urlopen("https://api.m.panda.tv/ajax_get_live_list_by_cate?pageno=1&pagenum=10&__plat=h5&cate=yzdr")
    for item in json.loads(html.read().decode('utf-8'))["data"]["items"]:
        print(item)


if __name__ == '__main__':
    getIndexPerson()
