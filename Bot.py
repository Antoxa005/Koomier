import pygame

class Bot:
    def __init__(self, startX, startY, width, height, tileWidth, tileHeight, color, listOfTiles):
        self.rect = pygame.Rect(startX, startY, width, height)

        self.tileWidth = tileWidth
        self.tileHeight = tileHeight

        self.listOfTiles = listOfTiles

        #self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), width, height)
        self.color = color

        self.broken = False
        self.movementEnabled = False

    def FindTile(self):
        for tile in self.listOfTiles:
            if tile.rect.centerx == self.rect.centerx and tile.rect.centery == self.rect.centery:
                return tile

    def Down(self):
        if not self.FindTile().wallSouth:
            self.rect.y += 80
            if self.FindTile() != None:
                if self.FindTile().wallNorth:
                    self.rect.y -= 80
            else:
                self.rect.y -= 80
    def Up(self):
        if not self.FindTile().wallNorth:
            self.rect.y -= 80
            if self.FindTile() != None:
                if self.FindTile().wallSouth:
                    self.rect.y += 80
            else:
                self.rect.y += 80
    def Left(self):
        if not self.FindTile().wallWest:
            self.rect.x -= 80
            if self.FindTile() != None:
                if self.FindTile().wallEast:
                    self.rect.x += 80
            else:
                self.rect.x += 80
    def Right(self):
        if not self.FindTile().wallEast:
            self.rect.x += 80
            if self.FindTile() != None:
                if self.FindTile().wallWest:
                    self.rect.x -= 80
            else:
                self.rect.x -= 80
    def Color(self):
        self.FindTile().Color((255, 0, 0))

    def DeColor(self):
        self.FindTile().DeColor()

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

class Button:
    def __init__(self, x, y, width, height, func):
        self.func = func
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)

    def OnClick(self, point):
        if self.rect.collidepoint(point):
            self.func()

pygame.init()
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
window = pygame.display.set_mode((screenWidth, screenHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)

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

def ResetButtonClick():
    bot.rect.x, bot.rect.y = 20, 20
    ansCode.clear()
    for tile in listOfTiles:
        tile.DeColor()
def PrintButtonClick():
    print("--------------------------------------")
    for ans in ansCode:
        print(ans)
    ansCode.clear()
def ToggleMoveButtonClick():
    if bot.movementEnabled:
        bot.movementEnabled = False
    else:
        bot.movementEnabled = True

listOfTiles = []
for x in range(640, -80, -80):
    for y in range(640, -80, -80):
        tile = Tile(x, y, 80, 80, (0, 255, 0), False, False, False, False, False, False, False, False)
        listOfTiles.append(tile)
bot = Bot(20, 20, 40, 40, 80, 80, (0, 0, 0), listOfTiles)
run = True
ansCode = []

ResetButton = Button(800, 10, 80, 80, ResetButtonClick)
PrintButton = Button(900, 10, 80, 80, PrintButtonClick)
ToggleMoveButton = Button(1000, 10, 80, 80, ToggleMoveButtonClick)
listOfButtons = [ResetButton, PrintButton, ToggleMoveButton]

for tile in listOfTiles:
    if tile.rect.x == 0:
        tile.wallWest = True
    if tile.rect.y == 0:
        tile.wallNorth = True
    if tile.rect.x == 640:
        tile.wallEast = True
    if tile.rect.y == 640:
        tile.wallSouth = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False

            if bot.movementEnabled:
                if keys[pygame.K_w] and bot.FindTile().wallNorth == False:
                    ansCode.append("bot.Up()")
                    bot.rect.y -= 80
                    if bot.FindTile().wallSouth:
                        bot.rect.y += 80
                elif keys[pygame.K_s] and bot.FindTile().wallSouth == False:
                    ansCode.append("bot.Down()")
                    bot.rect.y += 80
                    if bot.FindTile().wallNorth:
                        bot.rect.y += 80
                elif keys[pygame.K_a] and bot.FindTile().wallWest == False:
                    ansCode.append("bot.Left()")
                    bot.rect.x -= 80
                    if bot.FindTile().wallEast:
                        bot.rect.x += 80
                elif keys[pygame.K_d] and bot.FindTile().wallEast == False:
                    ansCode.append("bot.Right()")
                    bot.rect.x += 80
                    if bot.FindTile().wallWest:
                        bot.rect.x -= 80
                if keys[pygame.K_SPACE]:
                    if bot.FindTile().isColored == True:
                        ansCode.append("bot.DeColor()")
                        bot.DeColor()
                    else:
                        ansCode.append("bot.Color()")
                        bot.Color()

        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()

            if left:
                mousePos = pygame.mouse.get_pos()
                for button in listOfButtons:
                    button.OnClick(mousePos)

    mousePos = pygame.mouse.get_pos()

    for button in listOfButtons:
        if button.rect.collidepoint(mousePos):
            button.color = (100, 100, 100)
        else:
            button.color = (0, 0, 0)

    window.fill((255, 255, 255))

    UpdateTiles(listOfTiles)
    pygame.draw.rect(window, bot.color, bot.rect)

    for button in listOfButtons:
        pygame.draw.rect(window, button.color, button.rect)

    pygame.display.update()
pygame.quit()