import random
while True:
        print("Rules:-\n"
              "1- Your number should lesser than 100.\n"
              "2- you will have only 9 chances.\n"
              "3- You just need to guess a random number.\n"
              "4- It will tell you greater or smaller.\n"
              "5- if greater, guess more greater number and if \n"
              "  smaller, guess more smaller number.\n")

        number = random.randint(1, 100)
        print("you have 9 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a == number:
            print("You Won!")
            exit()

        print("you have 8 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()


        print("you have 7 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()

        print("you have 6 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()

        print("you have 5 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()

        print("you have 4 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()

        print("you have 3 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()

        print("you have 2 chances only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won")
            exit()

        print("you have last chance only!")
        a = int(input("Guess Number\n"))
        if a > number:
            print("Small number")
        if a < number:
            print("Greater number")
        if a > 100:
            print("Limit is under 50")
        elif a== number:
            print("You Won!")
            exit()


        print("\nBetter luck Next Time.....")
        print("The Number was...", number)

        play_again = input("\n\nDo you want to play again?\n"
                           "Enter here yes or no:-  ")
        if play_again== "yes":
            pass

        elif play_again== "no":
            break

        else:
            print("Invalid Input")
            exit()