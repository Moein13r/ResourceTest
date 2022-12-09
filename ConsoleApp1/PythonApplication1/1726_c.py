def GetClosedBrocket(start, s) -> int:
    tempStack = []
    for i in range(start, len(s), 1):
        if s[i] == ')':
            if len(tempStack) == 0:
                return i
            tempStack.pop()
        else:
            tempStack.append('(')
    return -1


tempStack2 = dict[int,int]


def GetClosedBrocket2(start, s) -> int:
    tempStack = [int,int]
    global tempStack2
    for i in range(start, len(s), 1):
        if s[i] == ')':
            if len(tempStack) == 0:
                return i
            tempStack.pop()
        else:
            tempStack2[len(tempStack)]+=1
            tempStack.append('(')
    return -1


t = int(input())
while t:
    n = int(input())
    s = input()
    TempGraph = []
    i = 0
    s2 = s
    while i < len(s2):
        if s2[i] == '(':
            index = GetClosedBrocket2(i+1, s2)
            TempGraph.append(s2[i+1:index])
            i = index-1
        i += 1
    print(TempGraph)
    print(tempStack2.values())
    t -= 1
