import pygame
import numpy as np



def EquationMaker(point1, point2):
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    if x1 == x2:
        return ("x", x1, None, None)

    if y1 == y2:
        return ("y", 0, y1, None)

    slopeX = x1 - x2
    slopeY = y1 - y2

    k = (slopeY / slopeX)
    b = y1 - k * x1

    if y1 > y2:
        return ("y", k, b, x2 < x1)
    else:
        return ("y", k, b, x2 > x1)

def PointChecker(equation, point):
    k = equation[1]
    b = equation[2]

    XorY = equation[0]
    slope = equation[3]

    x = point[0]
    y = point[1]

    if XorY == "x":
        if x >= k:
            return True
        else:
            return False

    if slope == None:
        if y >= b:
            return True
        else:
            return False

    elif slope:
        newY = k * x + b
        if newY <= y:
            return True
        else:
            return False

    else:
        newY = -k * x + b
        if newY <= y:
            return True
        else:
            return False

def calculate(point1, point2, point3, checkpoint):
    equation1 = EquationMaker(point1, point2)
    equation2 = EquationMaker(point1, point3)
    equation3 = EquationMaker(point3, point2)

    slope1 = equation1[3]
    slope2 = equation2[3]
    slope3 = equation3[3]

    point = checkpoint

    check1 = PointChecker(equation1, point)
    check2 = PointChecker(equation2, point)
    check3 = PointChecker(equation3, point)

    if (check1 == check2 and check1 != check3) or (check3 == check2 and check1 != check3) or (check1 == check3 and check1 != check2):
        return "In"
    else:
        return "Out"

#point1 = list(map(int, input().split()))
#point2 = list(map(int, input().split()))
#point3 = list(map(int, input().split()))
#point4 = list(map(int, input().split()))

#print(calculate(point1,
#point2,
#point3,
#point4))








#print(L1)
#print(RunAll(a, L1))
#print(GenerateRun(RunAll(a, L1)))
#print(GenerateAll(a, RunAll(a, L1)))



pygame.init()
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
window = pygame.display.set_mode((screenWidth, screenHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)

run = True

kelp = True


def GetPoints(f, numOfPoints, a, b):
    listOfPoints = []

    for i in range(0, numOfPoints):
        x = a + i * (b - a) / numOfPoints
        y = f(x)
        listOfPoints.append((x, y))


    return listOfPoints


def ConvertToScreen(listOfPoints, a, b, c, d):
    newPointList = []
    for point in listOfPoints:
        x = point[0]
        y = point[1]

        screenX , screenY = (x - a) * screenWidth / (b - a), (y - c) * screenHeight / (d - c)

        newPoint = (screenX, screenY)
        newPointList.append(newPoint)

    return newPointList

def PlotGraph(listOfPoints):
    for point in listOfPoints:
        index = listOfPoints.index(point)

        if len(listOfPoints) > index + 1:
            point2 = listOfPoints[index+1]
            pygame.draw.line(window, (255, 0, 0), point, point2, 5)

            pygame.display.update()

            #print(point2)
            #print(point)
            #print()


def f1(x):
    return np.sin(x)

def f2(x):
    return -np.sin(x)

d = -5


a = -10
b = 10
c = 5

a = -screenWidth / 100
b = screenWidth / 100
c = screenHeight / 100
d = -screenHeight / 100



points1 = GetPoints(f1, 100, a, b)

convertedPoints1 = ConvertToScreen(points1, a, b, c, d)

points2 = GetPoints(f2, 100, a, b)

convertedPoints2 = ConvertToScreen(points2, a, b, c, d)


window.fill((0, 0, 0))

pygame.draw.line(window, (255, 255, 255), (screenWidth / 2, screenHeight), (screenWidth / 2, 0), 5)
pygame.draw.line(window, (255, 255, 255), (screenWidth, screenHeight / 2), (0, screenHeight / 2), 5)


PlotGraph(convertedPoints1)
PlotGraph(convertedPoints2)





pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
pygame.quit()
