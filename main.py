import os, time, random


def Add():
  os.system("clear")
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")


def Show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")


while True:
  print("🌟Idea Storage🌟")
  print()
  menu = input("1: Add an idea\n2: Load up a random idea\n> ")
  if menu == "1":
    Add()
  elif menu == "2":
    Show()

  else:
    print("Invalid input")
    time.sleep(1)
    os.system("clear")
