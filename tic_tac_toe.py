from helper import check_rows,check_cols,check_left_diagonal,check_right_diagonal
import os
import time
os.system("cls" if os.name == "nt" else "clear")

class Player():
    '''Represents a player in game'''
    all_players = []
    def __new__(cls,name,symbol):
        for player in cls.all_players:
            if player.name == name:
                return player  
        return super().__new__(cls)

    def __init__(self, name: str, symbol: str):
        if not hasattr(self, 'name'): 
            self.name = name
            self.symbol = symbol
            self.games_won = 0
            self.games_drawn = 0
            self.games_lost = 0
            Player.all_players.append(self)

    def get_score(self):
        print(f"{self.name}'s stats")
        print(f"Games Won: {self.games_won}")
        print(f"Games Drawn: {self.games_drawn}")
        print(f"Games Lost: {self.games_lost}")

    @classmethod
    def highscore(cls):
        sorted_players = sorted(cls.all_players, key=lambda player: player.games_won, reverse=True)
        print("High Scores:")
        for player in sorted_players[:5]:
            print(f"{player.name} - Games Won: {player.games_won}")

class Board():
    _id_counter = 1
    def __init__(self,row:int,col:int):
        self.cells=[[" " for _ in range(col)] for _ in range(row)]
        Board._id_counter+=1
    
    def display_board(self):
        for i in range(len(self.cells)):
            row_str=""
            for j in (range(len(self.cells[0]))):
                row_str += f"|{self.cells[i][j]}|"
            print(row_str)
            for _ in range(len(self.cells[0])):
                print("---",end="")
            print("")

    def valid_move(self,row:int,col:int)->bool:
        '''Checking if move is valid or not'''
        if 0 <= col < len(self.cells[0]) and 0 <= row < len(self.cells) and self.cells[row][col] == " ":
            return True 
        return False

    def make_move(self,row:int,col:int,symbol:str):
        if self.valid_move(row,col):
            self.cells[row][col]=symbol
            return True
        return False
    def check_winner(self,symbol:str)->bool:
        '''Checking if current symbol player has won or not'''

        '''Checking if player has won with rows'''
        if check_rows(self.cells,symbol):
            return True
        '''Checking if player has won via collumns'''
        if check_cols(self.cells,symbol):
            return True
        '''Checking for left diagonal'''
        if check_left_diagonal(self.cells,symbol):
            return True
        '''Check right diagonal'''
        if check_right_diagonal(self.cells,symbol):
            return True
        
        return False
    def is_full(self)->bool:
        flag:bool=True
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j]==" ":
                    return False
        return True

class TicTacToe():
    '''Handles Whole game logic'''
    def __init__(self,player1:Player,player2:Player,row:int,col:int):
        self.board=Board(row,col)
        self.players=[player1,player2]
        self.current_player_index=0
    
    def switch_turn(self):
        self.current_player_index=1-self.current_player_index
    
    def play(self):
        '''Main Game loop'''
        print("Welcome to tic tac toe game:")
        self.board.display_board()
        while True:
            current_player=self.players[self.current_player_index]
            print(f"{current_player.name}'s trun {current_player.symbol}:")
            try:
                row,col=input("Please enter row and collumn you want to play 0 based indexing or press ctrl+c to exit :" ).split()
                row, col = map(int, (row, col))
            except ValueError:
                print("Invalid input")
                continue
            
            if self.board.make_move(row,col,current_player.symbol):
                self.board.display_board()
                if self.board.check_winner(current_player.symbol):
                    print(f"Congratulations, {current_player.name}! You win!")
                    current_player.games_won+=1
                    self.players[1-self.current_player_index].games_lost+=1
                    break
                if self.board.is_full():
                    print("The game is a draw!")
                    current_player.games_drawn+=1
                    self.players[1-self.current_player_index].games_drawn+=1
                    break
                self.switch_turn()
            else:
                print("invalid Move Try again")


    
    
if __name__ == "__main__":
    try:
        while True:
            row,col=(map(int,input("Please enter numbers of rows and columns you want to play seperated by space: ").split(" ")))
            p1=input("Player 1 name:")
            p2=input("Player 2 name:")
            player1 = Player(p1, "X")
            player2 = Player(p2, "O")
            game = TicTacToe(player1, player2,row,col)
            game.play()
            os.system("cls" if os.name == "nt" else "clear")
            player1.get_score()
            player2.get_score()
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                decision = input("Press y to play again, n to exit, s to see highscores: ").lower()
                if decision == "s":
                    Player.highscore()
                elif decision == "n":
                    print("Thanks for playing! Exiting...")
                    exit() 
                elif decision == "y":
                    break
                else:
                    print("Invalid input. Please enter y, n, or s.")
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        exit()