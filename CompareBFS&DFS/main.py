import random
import time
import csv

def main():
    dic = readData()
    dicBFS = sort(dic.copy(), "BFS")
    dicDFS = sort(dic.copy(), "DFS")
    pairs = randomPairs(dic)

    results = []
    for start, goal in pairs:
        timeDFS = timeMeasure(DFS_Goal, start, goal, dicDFS)
        timeBFS = timeMeasure(BFS_Goal, start, goal, dicBFS)
        results.append((start, goal, timeBFS, timeDFS))

    with open("Comparisons.csv", mode="w", newline='') as file:
        writer = csv.writer(file, delimiter="|")
        writer.writerow(["Start              |Goal                |BFS Time            |DFS Time            "])
        for start, goal, timeBFS, timeDFS in results:
            writer.writerow([f"{start:<20}", f"{goal:<20}", f"{timeBFS:<20}", f"{timeDFS:<20}"])
            
    print("Results have been written in Comparisons.csv file")

def readData():
    dic = {}
    with open("../Test 3.txt") as file:
        for line in file:
            row = line.rstrip().split("\t")
            key = int(row[0])
            value = int(row[1])
            if key not in dic:
                dic[key] = set()
            dic[key].add(value)
            if value not in dic:
                dic[value] = set()
            dic[value].add(key)
    return dic

def sort(dic , algorithm):
    for key in dic:
        values = list(dic[key])
        for i in range(len(values)):
            for j in range(i , len(values)):
                if algorithm == "BFS":
                    if (values[i] > values[j]):
                        values[i] , values[j] = values[j] , values[i]
                else :
                    if (values[i] < values[j]):
                        values[i] , values[j] = values[j] , values[i]
        dic[key] = values
    return dic

def randomPairs(dic, n=20):
    nodes = list(dic.keys())
    pairs = []
    for _ in range(n):
        start = random.choice(nodes)
        goal = random.choice(nodes)
        pairs.append((start, goal))
    return pairs

def timeMeasure(algorithm, start, goal, dic):
    start_time = time.time()
    algorithm(start, goal, dic)
    end_time = time.time()
    return end_time - start_time

def BFS_Goal(start, goal, dic): 
    V_F = []
    V_N = [start]
    while V_N:
        current = V_N.pop(0)
        if current not in V_F:
            V_F.append(current)
            if current == goal:
                break
            for i in dic[current]:
                if i not in V_F:
                    V_N.append(i)
    return V_F

def DFS_Goal(start, goal, dic): 
    V_F = []
    V_N = [start]
    while V_N:
        current = V_N.pop()
        if current not in V_F:
            V_F.append(current)
            if current == goal:
                break
            for i in dic[current]:
                if i not in V_F:
                    V_N.append(i)
    return V_F

main()
