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
game_choices = [rock,paper,scissors]
my_choice = int(input("Which one do you want? Enter 0 for rock, 1 for paper, 2 for scissors: "))
random_index = random.randint(0,2)
computer_choice = random_index
if my_choice<0 or my_choice>2:
    print("Please enter the valid number")
else:
    if my_choice == 0:
        print(f"I choose: {rock}")
    elif my_choice == 1:
        print(f"I choose: {paper}")
    elif my_choice == 2:
        print(f"I choose: {scissors}")
    print(f"Computer choose: {game_choices[computer_choice]}")
    if my_choice == computer_choice:
        print("We both draw.")
    elif my_choice == 0 and computer_choice == 1:
        print("You lose the game.")

    elif my_choice == 0 and computer_choice == 2:
        print("You win the game.")

    elif my_choice == 1 and computer_choice == 0:
        print("You win the game.")

    elif my_choice == 1 and computer_choice == 2:
        print("You lose the game.")

    elif my_choice == 2 and computer_choice == 0:
        print("You lose the game.")

    elif my_choice == 2 and computer_choice == 1:
        print("You win the game.")
