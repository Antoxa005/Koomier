from Bot import Bot
from Tiles import listOfTiles

side = 40
bot = Bot(side/4, side/4, side/2, side/2, side, side, (0, 0, 0), listOfTiles)
for tile in listOfTiles:
    if tile.startPoint:
        bot.rect.centerx = tile.rect.centerx
        bot.rect.centery = tile.rect.centery

        bot.newRect.centerx = tile.rect.centerx
        bot.newRect.centery = tile.rect.centery

        bot.ogX = tile.rect.x + side/4
        bot.ogY = tile.rect.y + side/4

def f1(bot): bot.Left()
def f2(bot): bot.Right()
def f3(bot): bot.Up()
def f4(bot): bot.Down()
def f5(bot): bot.Color()
def f6(bot): bot.DeColor()
def f7(bot):
    for i in range(3):
        f2(bot)
def f8(bot):
    for i in range(4):
        f4(bot)
def f9(bot):
    for i in range(4):
        f3(bot)
def f10(bot):
    for i in range(5):
        f4(bot)
def f11(bot):
    for i in range(3):
        f1(bot)
def f12(bot):
    for i in range(11):
        f2(bot)
def Run(bot):
    f5(bot)
    f7(bot)
    f5(bot)
    f8(bot)
    f5(bot)
    f4(bot)
    f2(bot)
    f5(bot)
    f7(bot)
    f5(bot)
    f2(bot)
    f3(bot)
    f5(bot)
    f9(bot)
    f5(bot)
    f7(bot)
    f5(bot)
    f8(bot)
    f5(bot)
    f10(bot)
    f5(bot)
    f8(bot)
    f5(bot)
    f11(bot)
    f5(bot)
    f9(bot)
    f5(bot)
    f3(bot)
    f1(bot)
    f5(bot)
    f11(bot)
    f5(bot)
    f1(bot)
    f4(bot)
    f5(bot)
    f8(bot)
    f5(bot)
    f11(bot)
    f5(bot)
    f9(bot)
    f5(bot)
    f3(bot)
    f12(bot)
    f10(bot)


Run(bot)


from Main import *
