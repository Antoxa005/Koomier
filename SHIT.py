import math

def calculate(a):
    a += 1
    return a

g = 10
answer = calculate(g)
print(answer)

a = {1: 'bot.Left()', 2: 'bot.Right()', 3: 'bot.Up()', 4: 'bot.Down()', 5: 'bot.Color()', 6: 'bot.DeColor()'}

print(list(a.values()))

L = ['bot.Down()', 'bot.Right()', 'bot.Down()', 'bot.Down()', 'bot.Right()', 'bot.Up()', 'bot.Up()', 'bot.Right()', 'bot.Down()', 'bot.Down()', 'bot.Right()', 'bot.Up()', 'bot.Up()', 'bot.Right()', 'bot.Down()', 'bot.Down()', 'bot.Right()']
L1 = []

def Convert(value, dict):
    return list(dict.keys())[list(dict.values()).index(value)]

def ConvertBack(key, dict):
    return list(dict.values())[list(dict.keys()).index(key)]

for i in L:
    L1.append(Convert(i, a))

print(list(L1))

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
    return array

def CheckIfTuple(element):
    L = [element]
    returnList = []
    for i in L:
        i = ConvertBack(i, a)
        if type(i) == str:
            returnList.append(i)

        else:
            for e in i[0]:
                L.append(e)

    return returnList



print(RunAll(a, L1))

#ans = RunAll(a, L1)

#realAns = []

print(CheckIfTuple(7))




    #if type(i) == tuple:
    #    oneLine = "for i in range(" + str(i[1]) + "): "
    #    while run:
    #        for e in i[0]:
    #            if e != 1 or e != 2 or e != 3 or e != 4 or e != 5 or e != 6:
    #                run = True
    #                i = e
    #            else:
    #                run = False


    #else:
    #    realAns.append(ConvertBack(i, a))






#print(GetComparand(L2, 0, 1))
