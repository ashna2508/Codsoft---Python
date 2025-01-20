import random
def computer():
    choices=["rock","paper","scissors"]
    return random.choice(choices)

def winner(user_c,comp_c):
    if user_c==comp_c:
        print("its a tie!!")
        
    elif (user_c=="rock" and comp_c=="scissors"):
        return "you win!"
    elif (user_c=="scissors" and comp_c=="paper"):
        return "you win!"
        
    elif (user_c=="paper" and comp_c=="rock"):
        return "you win!"
    else:
        return "you lose!"
def main():
    score_u=0
    score_c=0
    print("welcome to rock,paper,scissors!")
    while True:
        user_c=input("enter your choice:")
        if user_c not in ["rock","paper","scissors"]:
            print("invalid input,please choose rock,paper,scissors")
        comp_c=computer()
        print(f"\nyou chose:{user_c}")
        print(f"\ncomputer choice:{comp_c}")
        result=winner(user_c,comp_c)
        print(result)

        if result== "you win!":
            score_u+=1
        elif result=="you lose!":
            score_c+=1
        print(f"Score:you-{score_u}|Computer-{score_c}")
        play_again=input("\ndo you want to play again?(y/n):").lower()
        if play_again!='y':
            print("thanks for playing!")
            break
if __name__=="__main__":
    main()