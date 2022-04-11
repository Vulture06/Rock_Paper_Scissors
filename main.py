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

#Write your code below this line 👇
you=int(input("What do you choose? 0 for Rock,1 for Paper and 2 for Scissors: \n"))
pc=random.randint(0,2)
game=[rock,paper,scissors]
if you>=3:
  print("Wrong number enered,You Lose.")
else:
  print(game[you])
  print(f"PC Choose: {pc}")
  print(game[pc])
if pc>you:
  print("You Lose!!!!!")
elif pc==0 and you==2:
  print("You Lose!!!!!")
elif you>pc:
  print("Congratulations!!!!You Win.")
elif you==0 and pc==2:
  print("Congratulations!!!!You Win.")
else:
  print("Match Draw")
  




