import pygame
from Tiles import Tile
import pickle

class Brush:
    def __init__(self, onClick, name):
        self.onClick = onClick
        self.name = name

class Button:
    def __init__(self, x, y, width, height, func, color, name):
        self.func = func
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.ogColor = color
        self.name = name

side = 40
pygame.init()
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
window = pygame.display.set_mode((screenWidth, screenHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)

run = True
clock = pygame.time.Clock()

def MakeFont(fontName, size, write, color, x, y):
    font = pygame.font.SysFont(fontName, size)
    renderFont = font.render(write, True, color)
    window.blit(renderFont, (x, y))

def UpdateTiles(listOfTiles):
    for tile in listOfTiles:
        pygame.draw.rect(window, tile.color, tile.rect)
        if tile.wallNorth:
            pygame.draw.line(window, (0, 0, 150), (tile.rect.x, tile.rect.y), (tile.rect.x + tile.rect.width, tile.rect.y), 5)
        else:
            pygame.draw.line(window, (255, 255, 0), (tile.rect.x, tile.rect.y), (tile.rect.x + tile.rect.width, tile.rect.y), 5)
        if tile.wallSouth:
            pygame.draw.line(window, (0, 0, 150), (tile.rect.x, tile.rect.y + tile.rect.height), (tile.rect.x + tile.rect.width, tile.rect.y + tile.rect.height), 5)
        else:
            pygame.draw.line(window, (255, 255, 0), (tile.rect.x, tile.rect.y + tile.rect.height), (tile.rect.x + tile.rect.width, tile.rect.y + tile.rect.height), 5)
        if tile.wallWest:
            pygame.draw.line(window, (0, 0, 150), (tile.rect.x, tile.rect.y), (tile.rect.x, tile.rect.y + tile.rect.height), 5)
        else:
            pygame.draw.line(window, (255, 255, 0), (tile.rect.x, tile.rect.y), (tile.rect.x, tile.rect.y + tile.rect.height), 5)
        if tile.wallEast:
            pygame.draw.line(window, (0, 0, 150), (tile.rect.x + tile.rect.width, tile.rect.y), (tile.rect.x + tile.rect.width, tile.rect.y + tile.rect.height), 5)
        else:
            pygame.draw.line(window, (255, 255, 0), (tile.rect.x + tile.rect.width, tile.rect.y), (tile.rect.x + tile.rect.width, tile.rect.y + tile.rect.height), 5)

        if tile.needsToBeColored and not tile.isColored:
            pygame.draw.circle(window, (200, 200, 200), (tile.rect.centerx, tile.rect.centery), side/8)

        if tile.startPoint:
            MakeFont("A", 20, "A", (0, 0, 0), tile.rect.centerx, tile.rect.centery)
        if tile.endPoint:
            MakeFont("B", 20, "B", (0, 0, 0), tile.rect.centerx - 10, tile.rect.centery - 10)


def OnWallBrushClick():
    allDistances = [mouseX - theTile.rect.left, theTile.rect.right - mouseX, mouseY - theTile.rect.top, theTile.rect.bottom - mouseY]
    minDistance = min(allDistances)

    print("POG")


    if minDistance == allDistances[0]:
        theTile.wallWest = True
        index = listOfTiles.index(theTile)
        if index <= len(listOfTiles) - 18:
            listOfTiles[index+17].wallEast = True
    if minDistance == allDistances[1]:
        theTile.wallEast = True
        index = listOfTiles.index(theTile)
        if index >= 17:
            listOfTiles[index-17].wallWest = True
    if minDistance == allDistances[2]:
        theTile.wallNorth = True
        index = listOfTiles.index(theTile)
        if index <= len(listOfTiles) - 2:
            listOfTiles[index+1].wallSouth = True
    if minDistance == allDistances[3]:
        theTile.wallSouth = True
        index = listOfTiles.index(theTile)
        if index >= 1:
            listOfTiles[index-1].wallNorth = True

def NeedsToBeColoredBrushOnClick():

    theTile.needsToBeColored = True

def EraseBrushOnClick():
    theTile.needsToBeColored = False
    theTile.startPoint = False
    theTile.endPoint = False

    theTile.wallWest = False
    index = listOfTiles.index(theTile)
    if index <= len(listOfTiles) - 18:
        listOfTiles[index+17].wallEast = False
    theTile.wallEast = False
    index = listOfTiles.index(theTile)
    if index >= 17:
        listOfTiles[index-17].wallWest = False
    theTile.wallNorth = False
    index = listOfTiles.index(theTile)
    if index <= len(listOfTiles) - 2:
        listOfTiles[index+1].wallSouth = False
    theTile.wallSouth = False
    index = listOfTiles.index(theTile)
    if index >= 1:
        listOfTiles[index-1].wallNorth = False


def StartPointBrushClick():
    for tile in listOfTiles:
        tile.startPoint = False
    theTile.startPoint = True

def EndPointBrushClick():
    for tile in listOfTiles:
        tile.endPoint = False
    theTile.endPoint = True


wallBrush = Brush(OnWallBrushClick, "wallBrush")
needsToBeColoredBrush = Brush(NeedsToBeColoredBrushOnClick, "needsToBeColoredBrush")
eraseBrush = Brush(EraseBrushOnClick, "eraseBrush")
startPointBrush = Brush(StartPointBrushClick, "startPointBrush")
endPointBrush = Brush(EndPointBrushClick, "endPointBrush")
listOfBrushes = [wallBrush, needsToBeColoredBrush, eraseBrush, startPointBrush, endPointBrush]

activeBrush = needsToBeColoredBrush

def wallBrushButtonClick():
    activeBrush = listOfBrushes[0]
    return activeBrush

def needsToBeColoredBrushButtonClick():
    activeBrush = listOfBrushes[1]
    return activeBrush

def eraseBrushButtonClick():
    activeBrush = listOfBrushes[2]
    return activeBrush

def endPointBrushButtonClick():
    activeBrush = listOfBrushes[3]
    return activeBrush

def startPointBrushButtonClick():
    activeBrush = listOfBrushes[4]
    return activeBrush

def saveLevelButtonOnClick():
    shit = []
    for tile in listOfTiles:
        shit.append((tile.rect.x, tile.rect.y, tile.rect.width, tile.rect.height, tile.color, tile.wallNorth, tile.wallSouth, tile.wallWest, tile.wallEast, tile.needsToBeColored, tile.isColored, tile.startPoint, tile.endPoint))
    pickle.dump(shit, open("Save", "wb"))

def discardLevelButtonOnClick():
    listOfTiles = []
    for x in range(side * 16, -side, -side):
        for y in range(side * 16, -side, -side):
            tile = Tile(x, y, side, side, (0, 255, 0), False, False, False, False, False, False, False, False)
            listOfTiles.append(tile)

    return listOfTiles


wallBrushButton = Button(1410, 10, 80, 80, wallBrushButtonClick, (255, 0, 0), "wall")
needsToBeColoredBrushButton = Button(1410, 110, 80, 80, needsToBeColoredBrushButtonClick, (0, 255, 0), "have to color")
eraseBrushButton = Button(1410, 210, 80, 80, eraseBrushButtonClick, (0, 0, 255), "erase")
startPointBrushButton = Button(1410, 310, 80, 80, startPointBrushButtonClick, (255, 255, 0), "start")
endPointBrushButton = Button(1410, 410, 80, 80, endPointBrushButtonClick, (165, 0, 255), "end")
saveLevelButton = Button(1410, 510, 80, 80, saveLevelButtonOnClick, (255, 0, 255), "save")
discardLevelButton = Button(1410, 610, 80, 80, discardLevelButtonOnClick, (50, 50, 50), "delete")

listOfButtons = [wallBrushButton, needsToBeColoredBrushButton, eraseBrushButton, startPointBrushButton, endPointBrushButton, saveLevelButton, discardLevelButton]

SaveList = pickle.load(open("Save", "rb"))
listOfTiles = []
for tile in SaveList:
    listOfTiles.append(Tile(tile[0], tile[1], tile[2], tile[3], tile[4], tile[5], tile[6], tile[7], tile[8], tile[9], tile[10], tile[11], tile[12]))
#for x in range(side * 16, -side, -side):
#    for y in range(side * 16, -side, -side):
#        tile = Tile(x, y, side, side, (0, 255, 0), False, False, False, False, False, False, False, False)
#        listOfTiles.append(tile)

while run:
    clock.tick(60)

    timeNew = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for button in listOfButtons:
                if button.rect.collidepoint(mousePos):
                    if (button == wallBrushButton or button == eraseBrushButton or button == needsToBeColoredBrushButton or button == startPointBrushButton or button == endPointBrushButton):
                        activeBrush = button.func()
                    elif button == discardLevelButton:
                        listOfTiles = button.func()
                    else:
                        button.func()

    left, middle, right = pygame.mouse.get_pressed(3)
    if left:
        mouseX, mouseY = pygame.mouse.get_pos()
        newMouseX, newMouseY = mouseX // side * side, mouseY // side * side

        for tile in listOfTiles:
            if tile.rect.x == newMouseX and tile.rect.y == newMouseY:
                theTile = tile
                helper = "Some"
                break
            else:
                helper = None


        if helper != None:
            activeBrush.onClick()



    mousePos = pygame.mouse.get_pos()
    for button in listOfButtons:
        if button.rect.collidepoint(mousePos):
            button.color = (100, 100, 100)
        else:
            button.color = button.ogColor



    window.fill((255, 255, 255))

    UpdateTiles(listOfTiles)

    for button in listOfButtons:
        pygame.draw.rect(window, button.color, button.rect)
        MakeFont("ButtonText", 20, button.name, (0, 0, 0), button.rect.centerx - 40, button.rect.centery)
    pygame.display.update()
pygame.quit()