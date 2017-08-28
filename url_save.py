# encoding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
import queue


# 获取标题
def getTitle(content_area):
    try:
        # print(content_area)
        dd_tag = content_area.find("dd", {"class": "lemmaWgt-lemmaTitle-title"})
        if dd_tag:
            return dd_tag.h1.get_text()
    except:
        print("title not found!")
        return None


# 获取概略信息
def getSummary(content_area):
    try:
        summary_tag = content_area.find("div", {"class": "lemma-summary"})
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


# 往队列中中添加链接
def add_all_links(content_area, link_queue):
    href_list = content_area.findAll("a", {"href": re.compile(r"^/item")})
    for href in href_list:
        if href.attrs["href"] not in link_set:
            link_queue.put(href.attrs["href"])
            # print(href)


# 写入文件
def writer_file(writer1, url, title, summary):
    writer1.writerow((url, title, summary))


def fetch_step(link_queue, base_url1, writer1):
    # 获取链接
    item_url1 = link_queue.get()
    # print(item_url1)
    html = urlopen(base_url + item_url1)
    bsObj1 = BeautifulSoup(html, "lxml")
    # 定位数据
    content_area = bsObj1.find("div", {"class": "main-content"})
    summary = getSummary(content_area)
    title = getTitle(content_area)
    print("词条:%s\n概述:%s" % (title, summary))
    # 添加链接
    add_all_links(content_area, link_queue)
    # 写数据
    writer_file(writer1, base_url1 + item_url1, title, summary)


csvFile = open("test.csv", "a+", errors="ignore")
base_url = "https://baike.baidu.com"
item_url = "/item/python"
queues = queue.Queue()
queues.put(item_url)
link_set = set()
link_set.add(item_url)
try:
    writer = csv.writer(csvFile)
    while True:
        fetch_step(queues, base_url, writer)
except Exception as e:
    print("error :%s" % e)
finally:
    csvFile.close()
