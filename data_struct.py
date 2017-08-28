graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["end"] = 5
graph["b"]["a"] = 3
graph["end"] = {}


costs = {}
infinity = float("inf")
costs["a"] = 6
costs["b"] = 2
costs["end"] =infinity

parents={}
parents["a"]="start"
parents["b"]="start"
parents["end"]=None

processed=[]

node=find_lowest_cost_node(costs)
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)
    node=find_lowest_cost_node(costs)


print(graph["start"].keys())
