from shutil import move
import pygame as pg 
from src.pieces import Game_State
from src.pieces import setup
from pprint import pprint

WIDTH = 804
HEIGHT = 804
DIMENSION = 8
SQ = HEIGHT // DIMENSION

FPSMAX = 15
SETTER = setup()
SETTER.Set_Pieces()

black_p = SETTER.black
white_p = SETTER.white

IMGS = {}
PIECES = {"wpawn", "bpawn", "wrook", "brook", "wknight", "bknight", "wbishop", "bbishop", "wqueen", "bqueen", "wking", "bking"}

def load_images():
    for piece in PIECES:
        IMGS[piece] = pg.transform.scale(pg.image.load(f"src/icons/{piece}.png"), (SQ, SQ))
                                         

def driver():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))

    gamestate = Game_State()

    load_images()
    running = True

    while running:
    
        for i in pg.event.get():
            if i.type == pg.QUIT:
                running = False
            elif i.type == pg.MOUSEBUTTONUP:
               SETTER.move(gamestate.board)

        draw_gamestate(screen, gamestate)
        
        clock.tick(FPSMAX)
        pg.display.flip()

def draw_gamestate(screen, gamestate):

    draw_board(screen)
    draw_pieces(screen, gamestate.board)

def draw_board(screen):
    colors = [pg.Color(238,238,210), pg.Color(118,150,86)] 
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            pg.draw.rect(screen,color,pg.Rect(c*SQ, r*SQ, SQ,SQ))

def draw_pieces(screen, gamestate):
    global SETTER
    global black_p
    global white_p
    
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            board_pos = gamestate[r][c]
            
            for i in range(len(black_p)):
                if black_p[i].position == board_pos:
                    pieces = f"b{black_p[i].name}"
                    screen.blit(IMGS[pieces], pg.Rect(c*SQ, r*SQ, SQ, SQ))
                    
            for i in range(len(white_p)):
                if white_p[i].position == board_pos:
                    pieces = f"w{white_p[i].name}"
                    screen.blit(IMGS[pieces], pg.Rect(c*SQ, r*SQ, SQ, SQ))
                