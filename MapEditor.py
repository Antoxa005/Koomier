import pygame
from Tiles import Tile


side = 40
pygame.init()
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
window = pygame.display.set_mode((screenWidth, screenHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)

run = True
clock = pygame.time.Clock()

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

listOfTiles = []
for x in range(side * 16, -side, -side):
    for y in range(side * 16, -side, -side):
        tile = Tile(x, y, side, side, (0, 255, 0), False, False, False, False, False, False, False, False)
        listOfTiles.append(tile)

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

    left, middle, right = pygame.mouse.get_pressed(3)
    if left:
        mouseX, mouseY = pygame.mouse.get_pos()
        newMouseX, newMouseY = mouseX // side * side, mouseY // side * side

        for tile in listOfTiles:
            if tile.rect.x == newMouseX and tile.rect.y == newMouseY:

                allDistances = [mouseX - tile.rect.left, tile.rect.right - mouseX, mouseY - tile.rect.top, tile.rect.bottom - mouseY]
                minDistance = min(allDistances)


                if minDistance == allDistances[0]:
                    tile.wallWest = True
                    index = listOfTiles.index(tile)
                    listOfTiles[index+17].wallEast = True
                if minDistance == allDistances[1]:
                    tile.wallEast = True
                    index = listOfTiles.index(tile)
                    listOfTiles[index-17].wallWest = True
                if minDistance == allDistances[2]:
                    tile.wallNorth = True
                    index = listOfTiles.index(tile)
                    listOfTiles[index+1].wallSouth = True
                if minDistance == allDistances[3]:
                    tile.wallSouth = True
                    index = listOfTiles.index(tile)
                    listOfTiles[index-1].wallNorth = True


                break



    window.fill((0, 0, 0))

    UpdateTiles(listOfTiles)


    pygame.display.update()
pygame.quit()