our_graph = {
    0:{1:100},
    1:{2:100, 3:600},
    2:{0:100, 3:200},
    3:{}
}

def shortestDistance(start:int, end:int) ->int:
    queue= []
    total_distances = {}
    queue.append(start)
    total_distances[start] = 0


    if start == end:
        return 0
    
    for iteration in range(len(our_graph)):
        nq = []
        while queue:
            current = queue.pop(0)
            for node in our_graph[current].keys():
                nq.append(node)

                if node in total_distances.keys():
                    total_distances[node] = min(total_distances[current] + our_graph[current][node], total_distances[node])
                else:
                    total_distances[node] = total_distances[current] + our_graph[current][node]
        queue = nq
    return total_distances[end]


print(shortestDistance(0,3))