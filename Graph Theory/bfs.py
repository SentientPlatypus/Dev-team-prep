our_graph = {
    0:[1, 5],
    1:[2, 4],
    2:[3],
    3:[0, 1],
    4:[3],
    5:[]
}




def shortestDistance(start:int, end:int) ->int:
    queue= []
    total_distances = {}
    queue.append(start)
    total_distances[start] = 0
    paths = []


    if start == end:
        return 0
    
    while queue:
        current = queue.pop(0)
        for node in our_graph[current]:
            if paths:
                for path in paths:
                    if path[-1] == current:
                        path.append(node)
            else:
                paths.append([current, node])
            queue.append(node)

            total_distances[node] = total_distances[current] + 1

            if node == end:
                print(paths)
                return total_distances[end]
    return -1


print(shortestDistance(0,3))