def bfs(graph, start, end):
    # BREADTH-FIRST-SEARCH
    # if ther is a way btw start and end
    visited = set()
    # not visited
    queue = []
    path_to = {}
    queue.append(start)
    visited.add(start)
    path_to[start] = None
    found = False
    path_length = 0

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            found = True
            break

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                path_to[neighbour] = current_node
                visited.add(neighbour)
                queue.append(neighbour)

        if found:
            while path_to[end] is not None:
                path_length += 1
                end = path_to[end]

    return path_length
