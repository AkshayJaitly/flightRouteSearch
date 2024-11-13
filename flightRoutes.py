from collections import deque

def bfs(flights, start, end):
    if start == end:
        return 0, [start]
    
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        city, path = queue.popleft()
        for neighbor in flights.get(city, []):
            if neighbor not in visited:
                if neighbor == end:
                    return len(path), path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return "No path exists", []

# Test
flights = {
    "BLR": ["DLI"],
    "GUR": ["MUM"],
    "MUM": ["CHN"],
    "CHN": ["DLI"]
}

start, end = "GUR", "DLI"
flights_count, path = bfs(flights, start, end)
print(f"Path from {start} to {end}: {path} with {flights_count} flights.")  # Path should exist with 2 flights
