import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


GAME = [rock, paper, scissors]
Player = int(input("Game is started for Rock press 0,paper press 1,scissors press 2.\n "))
if Player >= 3 or Player < 0:
	print("Invaid choice")
else:
	print(GAME[Player])

	computer = random.randint(0,2)
	print("computer chose")
	print(GAME[computer])


	if Player == 0 and computer == 2:
		print("You Win")
	elif computer == 2 and Player == 0:
		print("You lose")
	elif computer > Player:
		print("You lose")
	elif Player > computer:
		print("you win")
	elif computer == Player:
		print("Draw")
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.