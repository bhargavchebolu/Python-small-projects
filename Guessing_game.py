import random
colours= ["Red","blue","green","yellow","violet","black","white","orange","purple"]

while True:
      colour = colours[random.randint(0,len(colours)-1)]
      guess = input("I am thinking about a colour, can you guess?  ")

      while True:
          if(colour == guess.lower()):
              break
          else:
              guess = input("Nope, try again: ")

      print("You guessed it, I was thinking about", colour)

      play_again = input("Let's play again. Type 'No' to quit: ")

      if play_again.lower() == No:
          break

print(" Thank you for playing ")
