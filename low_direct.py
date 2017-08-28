from collections import deque


def is_end_m(name):
    print("检查%s是否是所需要的" % name)
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["tho1", "jonny"]
graph["peggy"] = {}
graph["anuj"] = {}
graph["tho1"] = {}
graph["jonny"] = {}
my_name = "you"
my_queue = deque()
my_set = set()
my_queue.append(my_name)
find_out=False
while my_queue.__len__() > 0:
    my_name = my_queue.pop()
    print("取出:%s检查" % my_name)
    my_set.add(my_name)
    for name in graph[my_name]:
        if is_end_m(name):
            print("%s是所需要的" % name)
            find_out=True
            break
        else:
            print("%s不是所需要的" % name)
            print("将%s关联的用户添加进队列" % name)
            my_queue.append(name)
    if find_out:
        break
print(my_queue)
print(my_set)