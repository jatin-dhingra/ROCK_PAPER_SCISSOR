import  random

def decide(user1,user2):
    if user1==user2:
        return None
    elif user1=="r":
        if(user2=="p"):
            return True
        elif(user2=="s"):
            return False
    elif user1=="p":
        if(user2=="r"):
            return False
        elif (user2=="s"):
            return True
    elif(user1=="s"):
        if(user2=="r"):
            return True
        elif(user2=="p"):
            return False


print("Welcome to Rock , Paper , Scissor Game: ")
print("player1 is computer and Player2 is you!")
name=input("Please enter you name: ")
print("Computer will choose randomly  rock(r), paper(p), scissor(s)")
choose=random.randint(1,3)
if choose==1:
    user1="r"
elif choose==2:
    user1="p"
elif choose==3:
    user1="s"
user2=input(f"{name} make a choice rock(r), paper(p), scissor(s)")

winner=decide(user1,user2)
print(f"computer choose: {user1}")
print(f"You choose: {user2}")
if(winner==None):
    print("Match Tied")
elif(winner):
    print(f"winner of the match is {name}!")
else:
    print("Winner of the match is Computer!")









