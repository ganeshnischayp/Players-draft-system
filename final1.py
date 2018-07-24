pref_team=[[1,0,4,2,3],[1,0,4,2,3],[3,0,1,4,2]]
pref_player=[[1,2,0],[2,1,0],[0,2,1],[2,0,1],[2,1,0]]
player=[[2,0,1],[2,1,0],[0,2,1],[1,2,0],[2,1,0]]
team=[0,1,2]
N=3
P=5
teamFree=[False for i in range(N)]
playerList=[-1 for i in range(P)]
def preference(a,b,c):
	if player[a][b]<player[a][c]:
		return True 
	else:
		return False
while (len(team)!=0):
	q=team.pop(0)
	for j in range(P):
		z=pref_team[q][j]
		if playerList[z]==-1:
			teamFree[q]=True
			playerList[z]=q
			break
		else:
			y=playerList[z]
			if preference(z,q,y)==True:
				team.append(y)
				teamFree[y]=False
				playerList[z]=q
				teamFree[q]=True
				break
player_List=["Virat","Dhoni","Smith","Rohit","Gambhir"]
team_List=["DD","RCB","KXIP"]
for i in range(5):
	if playerList[i]==-1:
		print(player_List[i],"-","None")
	else:
		print(player_List[i],"-",team_List[playerList[i]])


#print(teamFree)
#print(playerList) 
