import pygame
side = 40

class Tile:
    def __init__(self, x, y, width, height, color, wallNorth=False, wallSouth=False, wallWest=False, wallEast=False, needsToBeColored=False, isColored=False, startPoint=False, endPoint=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.ogColor = color

        self.startPoint = startPoint
        self.endPoint = endPoint


        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
        self.walls = [wallNorth, wallSouth, wallWest, wallEast]

        self.wallNorth = wallNorth
        self.wallSouth = wallSouth
        self.wallWest = wallWest
        self.wallEast = wallEast

        self.needsToBeColored = needsToBeColored
        self.isColored = isColored


    def Color(self, newColor):
        self.isColored = True
        self.color = newColor

        self.image.fill(self.color)

    def DeColor(self):
        self.isColored = False
        self.color = self.ogColor

        self.image.fill(self.color)

listOfTiles = []
for x in range(side * 16, -side, -side):
    for y in range(side * 16, -side, -side):
        tile = Tile(x, y, side, side, (0, 255, 0), False, False, False, False, False, False, False, False)
        listOfTiles.append(tile)
for tile in listOfTiles:
    if tile.rect.x == 0:
        tile.wallWest = True
    if tile.rect.y == 0:
        tile.wallNorth = True
    if tile.rect.x == side * 16:
        tile.wallEast = True
    if tile.rect.y == side * 16:
        tile.wallSouth = True

    if tile.rect.x == 0 and tile.rect.y == 0:
        tile.startPoint = True

    if tile.rect.x == side * 16 and tile.rect.y == side * 16:
        tile.endPoint = True

    if tile.rect.x == side * 8:
        tile.needsToBeColored = True

    if tile.rect.y == side * 8:
        tile.needsToBeColored = True
