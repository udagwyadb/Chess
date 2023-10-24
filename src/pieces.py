import pygame as pg

STORED_PIECE = None
class Gamestate:
    def __init__(self) -> None:


        self.FILE = ["A", "B", "C", "D", "E", "F", "G", "H"]

        self.board = [
            ["brook", "bknight", "bbishop", "bqueen",
                "bking", "bbishop", "bknight", "brook"],
            ["bpawn", "bpawn", "bpawn", "bpawn",
                "bpawn", "bpawn", "bpawn", "bpawn"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wpawn", "wpawn", "wpawn", "wpawn",
                "wpawn", "wpawn", "wpawn", "wpawn"],
            ["wrook", "wknight", "wbishop", "wqueen",
                "wking", "wbishop", "wknight", "wrook"]
        ]
        self.whiteMove = True
        self.moves = []

    def move(self, gamestate) -> None:
        from src.renderer import SQ
        global STORED_PIECE

        movepos = pg.mouse.get_pos()
        movepos = list(movepos)
        movepos = [(movepos[0]//SQ), (movepos[1]//SQ)]

        y_cord = movepos[0]
        x_cord = movepos[1]
        movepos = tuple(movepos)

        print(movepos)

        gamestate

        if gamestate[x_cord][y_cord] != "--" and STORED_PIECE == None:
            STORED_PIECE = gamestate[x_cord][y_cord]
            self.storedpos = x_cord
            self.storedposy = y_cord
            gamestate[x_cord][y_cord] = "--"
            print(STORED_PIECE)

        elif gamestate[x_cord][y_cord] == "--":
            try:
                temp = STORED_PIECE[1:]
                if  temp == "pawn":
                    pawnstate = pawn(self.storedpos, self.storedposy)
                    legal = pawnstate.setup()
                    if [y_cord] in legal:
                        print(f"{STORED_PIECE} {self.FILE[x_cord]}{y_cord}")
                        gamestate[x_cord][y_cord] = STORED_PIECE
                        self.moves.append(
                            f"{STORED_PIECE} {self.FILE[x_cord]}{y_cord}")
                        STORED_PIECE = None
            except:
                print(STORED_PIECE[1:])
                print(f"{self.FILE[x_cord]}{y_cord}")

        elif gamestate[x_cord][y_cord] != "--" and STORED_PIECE != None:
            gamestate[x_cord][y_cord] = STORED_PIECE
            print(f"{STORED_PIECE}x{self.FILE[x_cord]}{y_cord}")
            self.moves.append(
                f"{STORED_PIECE}x{self.FILE[x_cord]}{y_cord}")
            STORED_PIECE = None


class pawn:
    def __init__(self, pos, posy) -> None:
        self.pos = pos
        self.posy = posy

    def setup(self):
        if self.pos != 6 and self.pos != 1:
            return self.move(self.posy)
        else:
            return self.extend_move(self.posy)

        # first satosfactory
        # second exellent
        # third proficent
        # last satisfactory
    def move(self, posy):
        legal_moves = []
        legal_moves.append(posy + 1)
        return legal_moves


    def extend_move(self,posy):
        legal_moves = []
        legal_moves.append(posy + 1); legal_moves.append(posy + 2)
        return legal_moves