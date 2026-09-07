import random
while True:
    choice=input("Guess Heads or Tails:").lower()
    result =random.choice(["heads","tails"])
    print("Coin landed on:",result)

    if choice == result:
        print("you won!")
    else:
     print("You lost!")

    again=input("play again?(Y/N):").lower()
    
    if again !="y":
        print("Game ended!")
        break

