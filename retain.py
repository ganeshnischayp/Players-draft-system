new=[]
count=0
player=["kohli","gayle","abd","rahul","chahal","negi"]
for i in range(len(player)):
	print(player[i])
t=input("enter the name of the player to be retained")
print(len(player))
for i in range(len(player)):
        a=player[i]
        if t==a:
                player[i]=None
for i in range(len(player)):
        if player[i]!=None:
               new[count]=player[i]
               count+=1
print(new)
