class Knight:

    def __init__(self, horizontal: str, vertical: int, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, x: str, y: int):
        doska1 = "87654321"
        doska2 = "abcdefgh"

        current_x = doska2.index(self.horizontal)
        current_y = doska1.index(str(self.vertical))
        new_pos_x = doska2.index(x)
        new_pos_y = doska1.index(str(y))

        if (current_x + 2 == new_pos_x and current_y - 1 == new_pos_y) or (current_x + 1 == new_pos_x and current_y - 2 == new_pos_y) or (current_x - 2 == new_pos_x and current_y - 1 == new_pos_y) or (
                current_x - 1 == new_pos_x and current_y - 2 == new_pos_y) or (current_x - 2 == new_pos_x and current_y + 1 == new_pos_y) or (
                current_x - 1 == new_pos_x and current_y + 2 == new_pos_y) or (current_x + 2 == new_pos_x and current_y + 1 == new_pos_y) or (current_x + 1 == new_pos_x and current_y + 2 == new_pos_y):
            return True
        else:
            return False


    def move_to(self, x, y):

        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y
        else:
            pass

    def draw_board(self):
        doska1 = "87654321"
        doska2 = "abcdefgh"

        board = [['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.', '.', '.']]

        l = doska1.index(str(self.vertical))
        k = doska2.index(str(self.horizontal))
        board[l][k] = self.get_char()

        for i in range(len(board)):
            for j in range(len(board)):
                pos_1 = (l-i)*(k-j)
                if pos_1 == 2 or pos_1 == -2:
                    board[i][j] = '*'

        for i in board:
            print(*i, sep='')



knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)


knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)


knight = Knight('c', 3, 'white')

knight.draw_board()