import pygame
from Grid import bot
from Tiles import listOfTiles
from SHIT import GenerateAll

side = 40

class Button:
    def __init__(self, x, y, width, height, func, color, name):
        self.func = func
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.ogColor = color
        self.name = name

    def OnClick(self, point):
        if self.rect.collidepoint(point):
            self.func()

pygame.init()
info = pygame.display.Info()
screenWidth, screenHeight = info.current_w, info.current_h
window = pygame.display.set_mode((screenWidth, screenHeight), pygame.HWSURFACE | pygame.DOUBLEBUF)

mainDict = {1: 'bot.Left()', 2: 'bot.Right()', 3: 'bot.Up()', 4: 'bot.Down()', 5: 'bot.Color()', 6: 'bot.DeColor()'}

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

        if tile.startPoint:
            MakeFont("A", 20, "A", (0, 0, 0), tile.rect.centerx, tile.rect.centery)
        elif tile.endPoint:
            MakeFont("B", 20, "B", (0, 0, 0), tile.rect.centerx, tile.rect.centery)
        if tile.needsToBeColored and not tile.isColored:
            pygame.draw.circle(window, (200, 200, 200), (tile.rect.centerx, tile.rect.centery), side/8)

        if tile.needsToBeColored and not tile.isColored:
            pygame.draw.circle(window, (200, 200, 200), (tile.rect.centerx, tile.rect.centery), side/8)

def UpdateButtons(listOfButtons):
    for button in listOfButtons:
        pygame.draw.rect(window, button.color, button.rect)
        MakeFont("ButtonText", 25, button.name, (0, 0, 0), button.rect.centerx - 40, button.rect.centery - 10)

def MakeFont(fontName, size, write, color, x, y):
    font = pygame.font.SysFont(fontName, size)
    renderFont = font.render(write, True, color)
    window.blit(renderFont, (x, y))

def ResetButtonClick():
    bot.rect.x, bot.rect.y = bot.ogX, bot.ogY
    bot.color = bot.ogColor
    bot.movementEnabled = False
    ansCode.clear()
    for tile in listOfTiles:
        tile.DeColor()
def PrintButtonClick():
    print("--------------------------------------")
    #for ans in ansCode:
    #    print(ans)
    #ansCode.clear()
    numAnsCode = []
    for i in ansCode:
        numAnsCode.append(Convert(i, mainDict))
    print(GenerateAll(mainDict, RunAll(mainDict, numAnsCode)))
    ansCode.clear()
def ToggleMoveButtonClick():
    if bot.movementEnabled:
        bot.movementEnabled = False
    else:
        bot.movementEnabled = True
def TeleportButtonClick():
    bot.rect.x = bot.newRect.x
    bot.rect.y = bot.newRect.y
    if bot.broken:
        bot.color = bot.brokenColor
        print("ERROR: BOT BROKEN")

    for i in bot.path:
        if i[2] == True:
            tile1 = bot.FindTileByCoordinate(i[0]-side/4, i[1]-side/4)
            tile1.Color((255, 0, 0))
def StepByStepButtonClick():
    ResetButtonClick()
    for i in bot.path:
        pygame.time.wait(100)
        bot.rect.x = i[0]
        bot.rect.y = i[1]
        if i[2] == True:
            bot.OtherColor()
        window.fill((255, 255, 255))

        UpdateTiles(listOfTiles)

        pygame.draw.rect(window, bot.color, bot.rect)

        UpdateButtons(listOfButtons)

        pygame.display.update()
    if bot.broken:
        bot.color = bot.brokenColor
        print("ERROR: BOT BROKEN")
def CheckButtonClick():
    error = False
    TeleportButtonClick()
    if bot.broken:
        print("ERROR: BOT BROKEN")
        error = True
    for tile in listOfTiles:
        if tile.needsToBeColored and not tile.isColored:
            print("ERROR: TILE NOT COLORED AT", tile.rect.x, tile.rect.y)
            error = True

        if tile.endPoint:
            if bot.rect.centerx != tile.rect.centerx or bot.rect.centery != tile.rect.centery or (bot.rect.centerx != tile.rect.centerx and bot.rect.centery != tile.rect.centery):
                print("ERROR: BOT NOT AT END POINT")

                for t in listOfTiles:
                    if t.endPoint:
                        print("END POINT:", t.rect.x, t.rect.y)
                error = True

    if not error:
        print("NO ERRORS FOUND")

run = True
ansCode = []
clock = pygame.time.Clock()

ResetButton = Button(1410, 10, 80, 80, ResetButtonClick, (255, 165, 0), "reset")
PrintButton = Button(1410, 110, 80, 80, PrintButtonClick, (0, 255, 0), "print")
ToggleMoveButton = Button(1410, 210, 80, 80, ToggleMoveButtonClick, (0, 0, 255), "movement")
TeleportButton = Button(1410, 310, 80, 80, TeleportButtonClick, (255, 0, 255), "teleport")
StepByStepButton = Button(1410, 410, 80, 80, StepByStepButtonClick, (255, 0, 0), "step by step")
CheckButton = Button(1410, 510, 80, 80, CheckButtonClick, (255, 255, 0), "check errors")
listOfButtons = [ResetButton, PrintButton, ToggleMoveButton, TeleportButton, StepByStepButton, CheckButton]

MainTimeOld = pygame.time.get_ticks()
while run:
    MainTimeNew = pygame.time.get_ticks()
    if MainTimeNew - MainTimeOld < 4:
        pygame.time.wait(6 - (MainTimeNew - MainTimeOld))
    MainTimeOld = MainTimeNew
    clock.tick(60)



    timeNew = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
            if bot.movementEnabled:
                if keys[pygame.K_w]:
                    ansCode.append("bot.Up()")
                    bot.MoveUp()
                elif keys[pygame.K_s]:
                    ansCode.append("bot.Down()")
                    bot.MoveDown()
                elif keys[pygame.K_a]:
                    ansCode.append("bot.Left()")
                    bot.MoveLeft()
                elif keys[pygame.K_d]:
                    ansCode.append("bot.Right()")
                    bot.MoveRight()
                if keys[pygame.K_SPACE]:
                    if bot.MoveFindTile().isColored == True:
                        ansCode.append("bot.DeColor()")
                    else:
                        ansCode.append("bot.Color()")
                    bot.OtherColor()

        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()

            if left:
                mousePos = pygame.mouse.get_pos()
                for button in listOfButtons:
                    button.OnClick(mousePos)

    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()

    for button in listOfButtons:
        if button.rect.collidepoint(mousePos):
            button.color = (100, 100, 100)
        else:
            button.color = button.ogColor

    window.fill((255, 255, 255))

    UpdateTiles(listOfTiles)

    pygame.draw.rect(window, bot.color, bot.rect)

    UpdateButtons(listOfButtons)

    pygame.display.set_caption(str(clock.get_fps()))

    pygame.display.update()
pygame.quit()