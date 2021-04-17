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

option = True
you_score = 0
computer_score = 0
computer_election = random.randint(0, 2)
game_image = [rock, paper, scissors]

while option:
  computer_election = random.randint(0, 2)
  print(f"Your score: {you_score} / Computer score: {computer_score}")

  my_election = int(input("What do you choose? Type 0 for Rock. 1 for Paper or 2 for Scissors: \n"))
  if my_election >= 3 or my_election < 0:
    print("You type and invalid number!!")
    my_election = int(input("What do you choose? Type 0 for Rock. 1 for Paper or 2 for Scissors: \n"))
    continue

  print(game_image[my_election])

  print(f"Computer choose: ")
  print(game_image[computer_election])


  if my_election == 0 and computer_election == 2:
    print("You Win!!")
    you_score = you_score + 1
  elif computer_election > my_election:
    print("You Lose!!")
    computer_score = computer_score + 1
  elif computer_election == 0 and my_election == 2:
    print("You Lose!!")
    computer_score = computer_score + 1
  elif my_election > computer_election:
    print("You Win!!")
    you_score = you_score + 1
  elif computer_election == my_election:
    print("Draw!!")

  stop = input("You want to play again? 'Yes' or 'No': \n")
  if stop.lower() == "no":
    option = False
  else:
    continue