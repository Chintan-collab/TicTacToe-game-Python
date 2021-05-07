from players import HumanPlayer,ComputerPlayer
import time
class Tictatoe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner= None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | '+' | '.join(row)+' |')
            print(' +- +- +- +- +')
    @staticmethod
    def print_board_nums():
        number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | '+' | '.join(row)+' | ')
            print(' +- +- +- +- +')
    def available_moves(self):
        return[i for i,spot in enumerate(self.board) if spot==' ']
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return len(self.available_moves())
    def make_move(self,square,letter):
        if self.board[square] ==' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    def winner(self,square,letter):
        row=square//3
        row=self.board[row*3:(row+1)*3]
        if all([spot==letter for spot in row]):
            return True

        col=square%3
        col=[self.board[col+i*3] for i in range(3)]
        if all([spot==letter for spot in col]):
            return True

        if square%2==0:
            diagonallr = [self.board[i] for i in [0,4,8]]
            if all([spot ==letter for spot in diagonallr]):
                return True
            diagonalrl = [self.board[i] for i in [2,4,6]]
            if all([spot ==letter for spot in diagonalrl]):
                return True
        return False

def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_board_nums()
    letter='X'
    while game.empty_squares():
        if letter=='O':
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square:{square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print('Hurray '+letter +'wins!!')
                return letter
            letter = 'O' if letter=='X' else 'X'
        time.sleep(1)

    if print_game:
        print('It\'s a Tie!!')
if __name__ == '__main__':
    x_player= ComputerPlayer('X')
    o_player=HumanPlayer('O')
    t=Tictatoe()
    play(t,x_player,o_player,print_game=True)
