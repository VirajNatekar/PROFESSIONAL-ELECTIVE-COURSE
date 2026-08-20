from queue import PriorityQueue

graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 5), ('E', 12)],
    
    'C': [('F', 7), ('G', 10)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


heuristic = {
    'A': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 2,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    pq.put((heuristic[start], start))

    while not pq.empty():
        h, current = pq.get()




        if current in visited:
            continue

        print(current, end=" ")
        visited.add(current)

        if current == goal:
            print("\nGoal found!")
            return

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    print("\nGoal not found.")

best_first_search('A', 'G')