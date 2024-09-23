def main():
    readData()
    sort(dic)
    global V_F
    V_F = []
    DFS_Type = ""
    while DFS_Type not in ["G", "N", "g", "n"]:
        DFS_Type = input("If there is a Goal enter G/g and if there is not enter N/n: ")
    DFS_Type = DFS_Type.upper()
    start = int(input("Please enter the Starting node: "))
    if (DFS_Type =="G"):
        Goal = int(input("Please enter the Goal node: "))
        Order = DFS_Goal(start , Goal)
        print(Order)
    elif (DFS_Type == "N"):
        Order = DFS_All(start)  
        print(Order)

def readData():
    global dic
    dic = {}
    fileName = ""
    while fileName not in [1 , 2]:
        fileName = int(input("Please enter 1 if you want to text file Test 1 and enter 2 for testing file Test 2: "))
    with open(f"../Test {fileName}.txt") as file:
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

def sort(dic):
    for key in dic:
        values = list(dic[key])
        for i in range(len(values)):
            for j in range(i , len(values)):
                if (values[i] < values[j]):
                    values[i] , values[j] = values[j] , values[i]
        dic[key] = values
    return dic

def DFS_Goal(start , Goal): 
    V_F = []
    V_N = [start]
    while V_N:
        current = V_N.pop()
        if current not in V_F:
            V_F.append(current)
            if current == Goal:
                break
            for i in dic[current]:
                if i not in V_F:
                    V_N.append(i)
    return V_F

def DFS_All(start):
    V_N = [start]
    while(len(V_F) != len(dic)) :
        current = V_N.pop()
        if (current not in V_F):
            V_F.append(current)
            for i in dic[current]:
                if( i not in V_F):
                    V_N.append(i)
    return V_F

main()
