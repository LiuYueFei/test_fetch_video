from collections import deque


def person_is_seller(person):
    return person[-1] == 'm'


graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search_queue = deque()
search_queue += graph["you"]
i = 1
while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller,deep ", i)
    else:
        search_queue += graph[person]
        i = i + 1
