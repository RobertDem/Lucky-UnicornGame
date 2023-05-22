def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()
    if response == "yes" or response == "y":
      response = "Yes"
      return response
    elif response == "no" or response == "n":
      response = "No"
      return response
    else:
      print("please answer yes/no")


show_instructions = yes_no("Program: Have you played this game before? ")
print("you: {}".format(show_instructions))
print()
having_fun = yes_no("Program: Are you having fun? ")
print("you: {}".format(having_fun))
