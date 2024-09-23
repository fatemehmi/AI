def main():
    pairs , cities , graph = readData()
    print(cities)
    start = ""
    while start not in cities:
        start = input("Please enter the Starting node(Use the above list and make sure to enter the same name i.e first letter is capatalized):")    
    order = GBFS(start , graph , pairs) 
    print("Solution found:", order) 
    

def readData():
    pairs , cities , graph = [] , [] , {}
    with open(f"../Heuristic.txt") as file:
        for line in file:
            row = line.strip().split("/")
            if len(row) >= 2:
                city = row[0]
                distance = int(row[-1])
                pairs.append((city , distance))
                cities.append(city)
    with open(f"../Graph.txt") as file: 
        for line in file:
            row = line.strip().split("/")
            if len(row) >= 2:
                column = row[0].split("-")
                firstCity = column[0]
                secondCity = column[1]
                if firstCity not in graph:
                    graph[firstCity] = set()
                graph[firstCity].add(secondCity)
                if secondCity not in graph:
                    graph[secondCity] = set()
                graph[secondCity].add(firstCity)      
    return pairs , cities , graph

def heuristicCost(city, pairs):
    for pair in pairs:
        if pair[0] == city:
            return pair[1]
    return float('inf')

def GBFS(start, graph, pairs):
    solution = [start]
    while True:
        current = solution[-1]
        if current == "Bucharest":
            break
        node = None
        distance = float('inf')
        for city in graph[current]:
            h = heuristicCost(city, pairs)
            if h < distance:
                distance = h
                node = city
        if node is None:
            break 
        solution.append(node)
    return solution
main()
