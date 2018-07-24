from random import randint
option = ["rock","paper","scissor","lizard","spock"]
message = ["tie","comp won","you won"]

def decide_winner (user,comp):
  print(user)
  print(comp)
  if user == comp :
    print(message[0])

  elif user==option[0]:
    if comp==option[1] or comp==option[4]:
      print(message[1])
    elif comp==option[2] or comp==option[3]:
      print(message[2])

  elif user==option[1]:
    if comp==option[2] or comp==option[3]:
      print(message[1])
    elif comp==option[0] or comp==option[4]:
      print(message[2])

  elif user==option[2]:
    if comp==option[0] or comp==option[4]:
      print(message[1])
    elif comp==option[1] or comp==option[3]:
      print(message[2])

  elif user==option[3]:
    if comp==option[0] or comp==option[2]:
      print(message[1])
    elif comp==option[1] or comp==option[4]:
      print(message[2])

  elif user==option[4]:
    if comp==option[1] or comp==option[3]:
      print(message[1])
    elif comp==option[2] or comp==option[0]:
      print(message[2])

def play():
    try:
        i=int(input("enter rock, paper,scissor,lizard,spock"))-1
    except Exception as i:
        print("not a valid responce")
    user = option[i]
    comp = option[randint(-1,4)]
    decide_winner (user, comp)
play ()
