#main driver file; responsible for handling user input and displaying the current GameState object
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENTION = 8 #8x8
SQ_SIZE = HEIGHT // DIMENTION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #We can access an image by saying 'IMAGES['wp']'


#The main driver for our code. This will handle user input and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() #only do it once, before the whole loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


#responsible of all the graphics
def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highliting or move suggestions idk
    drawPieces(screen, gs.board) #draw pieces on top of squares


#Draw the squares on the board, the top left square is always light.
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range (DIMENTION):
        for c in range(DIMENTION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

#Draw the pieces on the moard using the current GameState.board
def drawPieces(screen, board):
    pass

if __name__ == "__main__":
    main()