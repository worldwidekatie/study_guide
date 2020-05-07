class Game:
    """
    A general representation of an 
    abstract game
    """
    fun_level = 5

    def __init__(self, player1='Alice', player2='Bob'):
        self.rounds = 2
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def print_player(self):
        """Print the players of the game"""
        print(self.player1, "is playing", self.player2)

    def add_round(self):
        self.current_round += 1
    
    def player1_score_add(self):
        self.player1_score += 1

    def player2_score_add(self):
        self.player2_score += 1
    
    def report_score(self):
        print(self.player1, "has", self.player1_score, "points and ",
        self.player2, "has ", self.player2_score, "points")


class TicTacToe(Games):
    """
    This is a child class from the games class
    """

    def __init__(self, rounds=5, player1='Will', player2='Mac'):

        super().__init__(rounds, player1, player2)
        self.x = self.player1
        self.o = self.player2

    def x_and_o(self):
        print(self.x, "is team X and", self.o, "is team O")
