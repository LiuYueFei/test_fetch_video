import re
from urllib.request import urlopen
import pymysql
from bs4 import BeautifulSoup
from collections import deque


# 获取标题
def getTitle(content_area):
    try:
        # print(content_area)
        dd_tag = content_area.find("dd", {"class": "lemmaWgt-lemmaTitle-title"})
        if dd_tag:
            print("get tag:%s" % dd_tag.h1.get_text())
            return dd_tag.h1.get_text()
    except:
        print("title not found!")
        return None


# 获取概略信息
def getSummary(content_area):
    try:
        summary_tag = content_area.find("div", {"class": "lemma-summary"})
        print("summary info:%s" % summary_tag.get_text())
        return summary_tag.get_text()
    except:
        print("summary not found!")
        return None


# 获取详细内容
def get_detail_content(content_area):
    content_arr = []
    try:
        for detail in content_area.findAll("div", {"label-module": "para"}):
            content_arr.append(detail.get_text())
            # print(detail.get_text())
        return content_arr
    except Exception as e:
        print("fetch detail content error :%s" % e)
        return None


# 获取所有链接
def get_links(content_area):
    href_list = content_area.findAll("a", {"href": re.compile(r"^/item")})
    # print("all links:%s" % href_list)
    href_arr = []
    for href in href_list:
        href_arr.append({"text": href.get_text(), "href": href.attrs["href"]})
        # print("text:%s,href:%s" % (href.get_text(), href.attrs["href"]))
    return href_arr


# 获取数据
def request_data(whole_url):
    print("request url:%s" % whole_url)
    html = urlopen(whole_url)
    bsObj = BeautifulSoup(html, "lxml")
    content_area = bsObj.find("div", {"class": "main-content"})
    return content_area


def store_in_mysql(cur, title, url, summary):
    if title != None and url != None and summary != None:
        cur.execute('INSERT INTO  t_baike (title, url,summary) VALUES ("%s","%s","%s")' % (
            title.replace("\"","").strip(), url.replace("\"","").strip(), summary.replace("\"","").strip()))
        cur.connection.commit()


conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE test")

base_url = "https://baike.baidu.com"
item_url = "/item/%E6%B5%B7%E6%B4%BE%E6%96%87%E5%8C%96"
# 请求 获得内容
content_area = request_data(base_url + item_url)
# 获取标题
getTitle(content_area)
# 获取概略信息
getSummary(content_area)
# 获取所有链接
href_arr = get_links(content_area)
my_set = set()
my_queue = deque()

my_set.add("python")
for href in href_arr:
    if href["text"] not in my_set:
        # print("text:%s,href:%s" % (href["text"], href["href"]))
        my_set.add(href["text"])
        my_queue.append(href["href"])
try:
    while my_queue.__len__() > 0:
        item_url = my_queue.popleft()
        # 请求 获得内容
        content_area = request_data(base_url + item_url)
        href_arr = get_links(content_area)

        store_in_mysql(cur, getTitle(content_area), item_url, getSummary(content_area))
        for href in href_arr:
            if href["text"] not in my_set:
                my_set.add(href["text"])
                my_queue.append(href["href"])
except Exception as e:
    print("exception:%s" % e)
    cur.close()
    conn.close()
