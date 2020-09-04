import random

print("\nWelcome! This is a simple rock-paper-scissors game!\n")


def game():
    while True:
        print("""\nEnter your choice:
                 - rock
                 - paper
                 - scissors""")
        user = str(input("Player's choice: "))

        options = ["rock", "paper", "scissors"]
        computer = random.choice(options)

        print("\nYou chose", user.upper(), "and the computer chose", computer.upper(), "\n")

        if user == "rock" and computer == "rock":
            print("It's a draw!")
            again()
        elif user == "rock" and computer == "paper":
            print("You lose!")
            again()
        elif user == "rock" and computer == "scissors":
            print("You win!")
            again()

        elif user == "paper" and computer == "paper":
            print("It's a draw!")
            again()
        elif user == "paper" and computer == "scissors":
            print("You lose!")
            again()
        elif user == "paper" and computer == "rock":
            print("You win!")
            again()

        elif user == "scissors" and computer == "scissors":
            print("It's a draw!")
            again()
        elif user == "scissors" and computer == "rock":
            print("You lose!")
            again()
        elif user == "scissors" and computer == "paper":
            print("You win!")
            again()

        else:
            print("\nWrong input. Choose again, please!\n")
            game()


def again():
    print("\nDo you want to play another round?\n")
    answer = str(input("\nEnter yes or no: "))
    if answer == "yes":
        game()
    elif answer == "no":
        print("\nThanks for playing! Have a nice day!")
        exit()
    else:
        print("\nWrong input! Choose again, please!\n")
        again()


def main():
    game()
    again()


main()




# class Game:
#     def __init__(self, id):
#         self.p1Went = False
#         self.p2Went = False
#         self.ready = False
#         self.id = id
#         self.moves = [None, None]
#         self.wins = [0,0]
#         self.ties = 0
#
#     def get_player_move(self, p):
#         """
#         :param p: [0,1]
#         :return: Move
#         """
#         return self.moves[p]
#
#     def play(self, player, move):
#         self.moves[player] = move
#         if player == 0:
#             self.p1Went = True
#         else:
#             self.p2Went = True
#
#     def connected(self):
#         return self.ready
#
#     def bothWent(self):
#         return self.p1Went and self.p2Went
#
#     def winner(self):
#
#         p1 = self.moves[0].upper()[0]
#         p2 = self.moves[1].upper()[0]
#
#         winner = -1
#         if p1 == "R" and p2 == "S":
#             winner = 0
#         elif p1 == "S" and p2 == "R":
#             winner = 1
#         elif p1 == "P" and p2 == "R":
#             winner = 0
#         elif p1 == "R" and p2 == "P":
#             winner = 1
#         elif p1 == "S" and p2 == "P":
#             winner = 0
#         elif p1 == "P" and p2 == "S":
#             winner = 1
#
#         return winner
#
#     def resetWent(self):
#         self.p1Went = False
#         self.p2Went = False
