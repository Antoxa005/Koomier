import pygame
side = 40

class Bot:
    def __init__(self, startX, startY, width, height, tileWidth, tileHeight, color, listOfTiles):
        self.rect = pygame.Rect(startX, startY, width, height)
        self.newRect = pygame.Rect(startX, startY, width, height)

        self.tileWidth = tileWidth
        self.tileHeight = tileHeight

        self.ogX = startX
        self.ogY = startY

        self.path = []

        self.listOfTiles = listOfTiles

        #self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), width, height)
        self.color = color
        self.ogColor = color
        self.brokenColor = (255, 0, 0)

        self.broken = False
        self.movementEnabled = False

    def MoveFindTile(self):
        for tile in self.listOfTiles:
            if tile.rect.centerx == self.rect.centerx and tile.rect.centery == self.rect.centery:
                return tile

    def MoveDown(self):
        if not self.MoveFindTile().wallSouth:
            self.rect.y += side
            if self.MoveFindTile() != None:
                if self.MoveFindTile().wallNorth:
                    self.rect.y -= side
            else:
                self.rect.y -= side
    def MoveUp(self):
        if not self.MoveFindTile().wallNorth:
            self.rect.y -= side
            if self.MoveFindTile() != None:
                if self.MoveFindTile().wallSouth:
                    self.rect.y += side
            else:
                self.rect.y += side
    def MoveLeft(self):
        if not self.MoveFindTile().wallWest:
            self.rect.x -= side
            if self.MoveFindTile() != None:
                if self.MoveFindTile().wallEast:
                    self.rect.x += side
            else:
                self.rect.x += side
    def MoveRight(self):
        if not self.MoveFindTile().wallEast:
            self.rect.x += side
            if self.MoveFindTile() != None:
                if self.MoveFindTile().wallWest:
                    self.rect.x -= side
            else:
                self.rect.x -= side

    #--------------------------------------------------------

    def FindTile(self):
        for tile in self.listOfTiles:
            if tile.rect.centerx == self.newRect.centerx and tile.rect.centery == self.newRect.centery:
                return tile

    def Down(self):
        if self.broken == False:
            if not self.FindTile().wallSouth:
                self.newRect.y += side
                if self.FindTile() != None:
                    if self.FindTile().wallNorth:
                        self.newRect.y -= side
                        self.broken = True
                else:
                    self.newRect.y -= side
                    self.broken = True
            else:
                self.broken = True
            self.path.append((self.newRect.x, self.newRect.y, False))

    def Up(self):
        if self.broken == False:
            if not self.FindTile().wallNorth:
                self.newRect.y -= side
                if self.FindTile() != None:
                    if self.FindTile().wallSouth:
                        self.newRect.y += side
                        self.broken = True
                else:
                    self.newRect.y += side
                    self.broken = True
            else:
                self.broken = True
            self.path.append((self.newRect.x, self.newRect.y, False))

    def Left(self):
        if self.broken == False:
            if not self.FindTile().wallWest:
                self.newRect.x -= side
                if self.FindTile() != None:
                    if self.FindTile().wallEast:
                        self.newRect.x += side
                        self.broken = True
                else:
                    self.newRect.x += side
                    self.broken = True
            else:
                self.broken = True
            self.path.append((self.newRect.x, self.newRect.y, False))

    def Right(self):
        if self.broken == False:
            if not self.FindTile().wallEast:
                self.newRect.x += side
                if self.FindTile() != None:
                    if self.FindTile().wallWest:
                        self.newRect.x -= side
                        self.broken = True
                else:
                    self.newRect.x -= side
                    self.broken = True
            else:
                self.broken = True
            self.path.append((self.newRect.x, self.newRect.y, False))

    def Color(self):
        self.path.append((self.newRect.x, self.newRect.y, True))

    def OtherColor(self):
        if not self.MoveFindTile().isColored:
            self.MoveFindTile().Color((255, 0, 0))
        else:
            self.MoveFindTile().DeColor()

    def ColorGivenTile(tile):
        tile.Color((255, 0, 0))

    def DeColor(self):
        tile = self.MoveFindTile()
        if not tile.isColored:
            self.path.append((self.newRect.x, self.newRect.y, True))
        else:
            self.path.append((self.newRect.x, self.newRect.y, False))

    def FindTileByCoordinate(self, x, y):
        for tile in self.listOfTiles:
            if tile.x == x and tile.y == y:
                return tile


