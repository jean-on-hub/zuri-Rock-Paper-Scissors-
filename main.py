from random import choice
options = ['R','P','S']
print('Pick between "R" for "rock", "P" for "paper", "S" for "scissors". ')
ans =input()
final = False
while  final ==False:
    while ans not in options :  
        ans = input('Pick between "R" for "rock", "P" for "paper", "S" for "scissors". ')
    cpuans = choice(["Rock","Paper","Scissors"])
    if ans  == 'R':
            ans = "Rock"
    elif ans == 'P':
        ans = "Paper"
    else:
        ans = "Scissors"


    if ans == cpuans:
        print(f"Both players selected {ans}. It's a tie! Try again")
        continue
    elif ans == "Rock":
        if cpuans == "scissors":
            print("Rock smashes scissors! You win!")
            final =True
        else:
            print("Paper covers Rock! You lose.")
            final =True
    elif ans == "paper":
        if cpuans == "Rock":
            print("Paper covers Rock! You win!")
            final =True
        else:
            print("Scissors cuts Paper! You lose.")
            final =True
    elif ans == "Scissors":
        if cpuans == "Paper":
            print("Scissors cuts Paper! You win!")
            final =True
        else:
            print("Rock smashes Scissors! You lose.")
            final =True
