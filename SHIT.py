import math

def calculate(a):
    a += 1
    return a

g = 10
answer = calculate(g)
print(answer)

a = {1: 'bot.Left()', 2: 'bot.Right()', 3: 'bot.Up()', 4: 'bot.Down()'}

print(list(a.values()))

L = ['bot.Down()', 'bot.Right()', 'bot.Down()', 'bot.Down()', 'bot.Right()', 'bot.Up()', 'bot.Up()', 'bot.Right()', 'bot.Down()', 'bot.Down()', 'bot.Right()', 'bot.Up()', 'bot.Up()', 'bot.Right()', 'bot.Down()', 'bot.Down()', 'bot.Right()']

def Convert(string):
    return a.get(string)

L1 = list(map(Convert, L))

L2 = [1, 2, 1, 2, 3, 4, 3, 4, 1, 2, 1, 2, 3, 4, 3, 4]

def Compare(array, comparand, startIndex):
    if startIndex + len(comparand) > len(array): return False

    for i in range(len(comparand)):
        if comparand[i] != array[startIndex+i]: return False

    return True

def GetComparand(array, startIndex, maxLen):
    returnList = []
    for i in range(startIndex, startIndex + maxLen): returnList.append(array[i])

    return returnList

def TryFindFirstPattern(array, maxLen):
    if maxLen * 2 > len(array): return (False, 0, 0, [], 0)

    for i in range(len(array) - 2 * maxLen + 1):
        comparand = GetComparand(array, i, maxLen)
        numOfRep = 0

        for e in range(i + maxLen, len(array) - maxLen + 1, maxLen):
            if not Compare(array, comparand, e): break
            numOfRep += 1

        if numOfRep > 0: return (True, i, i + maxLen * (numOfRep+1), comparand, numOfRep + 1)

    return (False, 0, 0, [], 0)

def ReplacePattern(dict, array, comparand, startIndex, endIndex, numOfRep):
    if (comparand, numOfRep) in list(dict.values()):
        key = list(dict.keys())[list(dict.values()).index((comparand, numOfRep))]
    else:
        helper = list(dict.keys())
        helper.reverse()
        newKey = int(helper[0]) + 1
        dict[newKey] = (comparand, numOfRep)
        key = newKey

    for i in range(startIndex, endIndex):
        print("Pog")
        print(i)
        array.pop(startIndex)

    array.insert(startIndex, key)

def RunOnce(dict, array, maxLen):
    changed = False
    while True:
        result = TryFindFirstPattern(array, maxLen)
        comparand = result[3]
        startIndex = result[1]
        endIndex = result[2]
        numOfRep = result[4]
        if not result[0]: return changed
        ReplacePattern(dict, array, comparand, startIndex, endIndex, numOfRep)
        changed = True

def RunMult(dict, array):
    maxLen = 1
    arrayLen = len(array)
    changed = False
    while True:
        changed = changed or RunOnce(dict, array, maxLen)
        maxLen += 1
        arrayLen = len(array)

        if maxLen * 2 > arrayLen: return changed

def RunAll(dict, array):
    result = True
    while result:
        result = RunMult(dict, array)
    print(array)

RunAll(a, L2)


#print(GetComparand(L2, 0, 1))
