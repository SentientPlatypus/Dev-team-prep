def bellmanford(graph, src):
    distances = {}

    for s, d, w in graph:
        distances[s] = float('Inf')
        distances[d] = float('Inf')
    
    n_of_nodes = len(distances.keys())
    print(distances)
    print(n_of_nodes)

    distances[src] = 0

    for _ in range(n_of_nodes - 1):
        for s, d, w in graph:
            if distances[s] != float('Inf') and distances[s] + w < distances[d]:
                print("updated %s to %s"%(d, distances[s] + w))
                distances[d] = distances[s] + w
    


    return distances

print(bellmanford(
    graph = [
        [0, 1, 100],
        [1, 2, 100],
        [1, 3, 600],
        [2, 0, 100],
        [2, 3, 200],
    ],
    src = 0
))
