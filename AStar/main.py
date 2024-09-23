def main():
    pairs, cities, connection = readData()
    print(cities)
    start = ""
    while start not in cities:
        start = input("Please enter the Starting node (Use the above list and make sure to enter the same name, i.e., first letter is capitalized): ")
    order = AStar(start, connection, pairs)
    print("Solution found:", order)

def readData():
    pairs, cities, connection = [], [], {}
    with open("../Heuristic.txt") as file:
        for line in file:
            row = line.strip().split("/")
            if len(row) >= 2:
                city = row[0]
                distance = int(row[-1])
                pairs.append((city, distance))
                cities.append(city)
    with open("../Graph.txt") as file: 
        for line in file:
            row = line.strip().split("/")
            if len(row) >= 2:
                distance = int(row[1])
                column = row[0].split("-")
                firstCity = column[0]
                secondCity = column[1]
                if firstCity not in connection:
                    connection[firstCity] = set()
                if secondCity not in connection:
                    connection[secondCity] = set()
                connection[firstCity].add((secondCity, distance))
                connection[secondCity].add((firstCity, distance))
    return pairs, cities, connection

def heuristicCost(city, pairs):
    for pair in pairs:
        if pair[0] == city:
            return pair[1]
    return float('inf')

def leastCostNode(openSet, pairs):
    leastCostIndex = 0
    leastCost = openSet[0][2] + heuristicCost(openSet[0][0], pairs)
    for i in range(1, len(openSet)):
        currentCost = openSet[i][2] + heuristicCost(openSet[i][0], pairs)
        if currentCost < leastCost:
            leastCost = currentCost
            leastCostIndex = i
    return openSet.pop(leastCostIndex)

def AStar(start, connection, pairs):
    openSet = [(start, [start], 0)]

    while True:
        current, path, cost = leastCostNode(openSet, pairs)

        if current == "Bucharest":
            return path

        for next, distance in connection[current]:
            newCost = cost + distance
            openSet.append((next, path + [next], newCost))

main()
