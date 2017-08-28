import re

i = 1
with open("socket.txt", encoding='utf-8', errors='ignore') as f:
    for line in f.readlines():
        if re.findall(r"线程", line):
            print("%s:%s" % (i, line.strip()))
            i = i + 1
