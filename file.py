import random
attempts_list=[]
def show_score():
    if len(attempts_list)==0:
        print("There is currently no high score , it's your for the taking ")
    else :
        print("The Current high score is {} ".format(min(attempts_list)))

def start_game():
    print("Welcome Traveller , Welcome to Guessing Game")
    print("What's your name ?")
    name = input()
    print("Hi {} , Want to Play Guess Game Enter Yes or no ".format(name))
    answer = input()
    show_score()
    attempt = 0
    number = random.randint(1, 10)
    while answer.lower() == 'yes':
        print("Pick a number between 1 and 10 ")
        try:
            guess = int(input())
            if guess > 10 or guess < 1:
                raise ValueError("That not a valid number between 1 and 10")
            if number == guess:
                print("Nice Work , It perfect !")
                attempt += 1
                attempts_list.append(attempt)
                print("It tooks you {} attempts".format(attempt))
                print("Do you want to play again ? Enter yes or no")
                answer = input()
                if answer.lower() == 'no':
                    print("Ok, See you again")
                    break
                else :
                    print("That's Cool , have a good one ")
                    show_score()
                    number = random.randint(1, 10)
                    attempt = 0
            elif number > guess:
                print("No , it greater than that")
                attempt += 1
            elif number < guess:
                print("No , it smaller than that")
                attempt += 1
        except ValueError as err:
            print("That's not a valid number !")
            print("({})".format(err))


if __name__=='__main__':
    start_game()





