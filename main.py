print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
if height > 120:
  print("You can ride the rolercoster")
  age = int(input("What is your age?\n"))
  if  age <= 18:
    print("Your ticket price is 7$")
  else:
    print("Your ticket price is 12$")
else:
  print("Can ride the rolercoster")
