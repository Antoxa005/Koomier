from bot import Bot
from Tiles import listOfTiles

side = 40
bot = Bot(side/4, side/4, side/2, side/2, side, side, (0, 0, 0), listOfTiles)

def f1(bot): bot.Left()
def f2(bot): bot.Right()
def f3(bot): bot.Up()
def f4(bot): bot.Down()
def f5(bot): bot.Color()
def f6(bot): bot.DeColor()
def f7(bot):
    for i in range(7):
        f4(bot)
def f8(bot):
    for i in range(2):
        f2(bot)
def f9(bot):
    for i in range(8):
        f5(bot)
        f2(bot)
def f10(bot):
    for i in range(8):
        f5(bot)
        f1(bot)
def f11(bot):
    for i in range(7):
        f5(bot)
        f1(bot)
def f12(bot):
    for i in range(4):
        f9(bot)
        f4(bot)
        f10(bot)
        f4(bot)
        f8(bot)
def Run(bot):
    f7(bot)
    f12(bot)
    f9(bot)
    f4(bot)
    f11(bot)
    f5(bot)

Run(bot)

from Main import *
