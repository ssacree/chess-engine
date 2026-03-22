#respinsible for storing all the information about the current state of a chess game; responsible for determening the valid moves at the current state; it can also keep a move log.
class GameState(): #GameState — это шаблон для создания объекта, который будет хранить состояние шахматной игры (доска, чей ход, история ходов).
    def __init__(self):
        #8x8 2d list, each element has 2 characters.
        #1st character=color
        #2nd character=piece
        #'--' represents an empty space.
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove = True
        self.movelog = []