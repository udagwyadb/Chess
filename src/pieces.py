import pygame as pg

STORED_PIECE = None
OBJ_STORER = None

class Game_State:
    def __init__(self) -> None:
        self.board = [
            ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"],
            ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
            ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6"],
            ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5"],
            ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"],
            ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],
            ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
            ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
        ]
        self.move_log = []
        self.turn = 1
    
    
                


class pawn:
    def __init__(self, color: str, position: str) -> None:

        self.color: str = color
        self.position: str = position
        self.name: str = "pawn"


class knight:
    def __init__(self, color: str, position: str) -> None:

        self.color: str = color
        self.position: str = position
        self.name: str = "knight"


class bishop:
    def __init__(self, color: str, position: str) -> None:

        self.color: str = color
        self.position: str = position
        self.name: str = "bishop"


class rook:
    def __init__(self, color: str, position: str) -> None:

        self.color: str = color
        self.position: str = position
        self.name: str = "rook"


class queen:
    def __init__(self, color: str, position: str) -> None:

        self.color: str = color
        self.position: str = position
        self.name: str = "queen"


class king:
    def __init__(self, color: str, position: str) -> None:

        self.color: str = color
        self.position: str = position
        self.name: str = "king"


class setup(Game_State):
    def __init__(self) -> None:
        super().__init__()

        self.black = []
        self.white = []
        self.legal = []

    def Set_Pieces(self):

        for row in self.board:
            if row[0][-1] == "8":
                for i in row:
                    if i[0] == "A" or i[0] == "H":
                        self.black.append(rook(color="B", position=i))
                    elif i[0] == "B" or i[0] == "G":
                        self.black.append(knight(color="B", position=i))
                    elif i[0] == "C" or i[0] == "F":
                        self.black.append(bishop(color="B", position=i))
                    elif i[0] == "D":
                        self.black.append(queen(color="B", position=i))
                    else:
                        self.black.append(king(color="B", position="E8"))

            elif row[0][-1] == "2":
                for i in row:
                    self.white.append(pawn(color="W", position=i))
            elif row[0][-1] == "7":
                for i in row:
                    self.black.append(pawn(color="B", position=i))
                    
            elif row[0][-1] == "1":
                for i in row:
                    if i[0] == "A" or i[0] == "H":
                        self.white.append(rook(color="W", position=i))
                    elif i[0] == "B" or i[0] == "G":
                        self.white.append(knight(color="W", position=i))
                    elif i[0] == "C" or i[0] == "F":
                        self.white.append(bishop(color="W", position=i))
                    elif i[0] == "D":
                        self.white.append(queen(color="W", position=i))
                    else:
                        self.white.append(king(color="W", position="E1"))
                        
            if len(self.black) and len(self.white) == 16:
                break

    def move(self, gamestate):
        from src.renderer import SQ
        global STORED_PIECE
        
        movepos = pg.mouse.get_pos()
        movepos = list(movepos)
        movepos = [(movepos[0]//SQ), (movepos[1]//SQ)]

        x_cord = movepos[0]
        y_cord = movepos[1]
        movepos = [x_cord, y_cord]
        print(movepos)
        movepos = tuple(movepos)
        
        print(movepos)
        
        self.mover(x_cord, y_cord, gamestate)
        
    def mover(self, x_cord, y_cord, gamestate):
        global STORED_PIECE
        global OBJ_STORER
            
        if STORED_PIECE == None:
            for i in range(len(self.black)):
                if gamestate[y_cord][x_cord] == self.black[i].position:
                    STORED_PIECE = self.black[i].position
                    OBJ_STORER = self.black[i]
                    print(STORED_PIECE, OBJ_STORER)
                    break
                
            for i in range(len(self.white)):
                if gamestate[y_cord][x_cord] == self.white[i].position:
                    STORED_PIECE = self.white[i].position
                    OBJ_STORER = self.white[i]
                    print(STORED_PIECE, OBJ_STORER)
                    break
        else:
            pos_check = f"{self.convert_to_alpha(x_cord)}{self.reverse_to_normal(y_cord)}"
            if OBJ_STORER.color == "W":
                checklist = [x for x in self.white if x.position == pos_check]
                if len(checklist) < 1:
                    self.move_checker(x_cord, y_cord)
                
            elif OBJ_STORER.color == "B":
                checklist = [x for x in self.black if x.position == pos_check]
                if len(checklist) < 1:
                    self.move_checker(x_cord, y_cord)
                
            OBJ_STORER = None
            STORED_PIECE = None
            
            
    def move_checker(self, x, y):
        global OBJ_STORER
        global STORED_PIECE
        
        if OBJ_STORER.name == "pawn":
            if OBJ_STORER.position[-1] == "2" and OBJ_STORER.color == "W":
                self.legal = [3, 4]
                
            elif OBJ_STORER.color == "W":
                self.legal = [int(OBJ_STORER.position[-1]) + 1]
                
                
            elif OBJ_STORER.position[-1] == "7" and OBJ_STORER.color == "B":
                self.legal = [6, 5]
                
            elif OBJ_STORER.color == "B":
                self.legal = [int(OBJ_STORER.position[-1]) - 1]
                
            
            x = OBJ_STORER.position[0]
            y = self.convert_to_cords(y, x)
            if y in str(self.legal):
                if OBJ_STORER.color == "W":
                    for i in range(len(self.white)):
                        if OBJ_STORER.position == self.white[i].position:
                            self.white[i].position =  f"{x}{y}"
                            STORED_PIECE = None
                            OBJ_STORER = None
                            self.legal = []
                            break
                else:
                    for i in range(len(self.black)):
                        if OBJ_STORER.position == self.black[i].position:
                            self.black[i].position =  f"{x}{y}"
                            STORED_PIECE = None
                            OBJ_STORER = None
                            self.legal = []
                            break
            
            else:
                STORED_PIECE = None
                OBJ_STORER = None
                self.legal = []
                return 0 
        
        elif OBJ_STORER.name == "rook":
            pass
        
        elif OBJ_STORER.name == "knight":
            from itertools import product
            
            temp_x = self.alpha_to_cords(OBJ_STORER.position[0])
            temp_y = int(OBJ_STORER.position[-1])
            
            legal = list(product([temp_x-1, temp_x+1],[temp_y-2, temp_y+2])) + list(product([temp_x-2,temp_x+2],[temp_y-1,temp_y+1]))
            legal = [(temp_x,temp_y) for temp_x,temp_y in legal if temp_x >= 0 and temp_y >= 0 and temp_x < 8 and temp_y < 8]
            
            
            x = self.convert_to_alpha(x)
            y = self.convert_to_cords(y, x)
            x = self.alpha_to_cords(x)
            y = int(y)
            for i in range(len(legal)):
                if x in legal[i] and y in legal[i]:
                    if OBJ_STORER.color == "W":
                        for j, p in enumerate(self.white):
                            if OBJ_STORER.position == self.white[j].position:
                                x = self.convert_to_alpha(x)
                                self.white[j].position =  f"{x}{y}"
                                STORED_PIECE = None
                                OBJ_STORER = None
                                self.legal = []
                                break
                        break
                    else:
                        for j, p in enumerate(self.black):
                            if OBJ_STORER.position == self.black[j].position:
                                x = self.convert_to_alpha(x)
                                self.black[j].position =  f"{x}{y}"
                                STORED_PIECE = None
                                OBJ_STORER = None
                                self.legal = []
                                break
                        break
            
            
        elif OBJ_STORER.name == "bishop":
            pass
        
        elif OBJ_STORER.name == "queen":
            pass
        
        else:
            pass
        
    
    def convert_to_cords(self, y, x):
        for i in range(len(self.board)):
            if i == y:
                for j in range(len(self.board[i])):
                    if self.board[i][j][0] == x:
                        y = self.board[i][j][-1]
                        return y
                    
    def alpha_to_cords(self,x):
        for i in range(len(self.board)):
            if self.board[0][i][0] == x:
                x = i
                return x
            
    def reverse_to_normal(self, y):
        convertion_base = [8, 7, 6, 5, 4, 3, 2, 1]
        y = int(y)
        tempy = convertion_base[y]
        return tempy
    
    def convert_to_alpha(self, x):
        convertion_base = ["A", "B", "C", "D", "E", "F", "G", "H"]
        x = convertion_base[x]
        return x 