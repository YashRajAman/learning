from collections import Counter\

#it is a chess tournament so a team can be of only 2 people.

def countTeams(rating, queries):
    teams_formed = []
    for x,y in queries:
        members = [rating[i] for i in range(x-1,y)]
        teams = dict(Counter(members))
        teams_counter = 0
        # print(teams)
        for mem in teams.values():
            if mem >= 2:
                teams_counter += mem // 2
        
        teams_formed.append(teams_counter)
    return teams_formed

ratings = [2,3,4,2]
queries = [[1,4], [3,4]]

ratings1 = [1,1]
queries1 = [[1,2], [1,1]]

ratings3 = [1,2]
queries3 = [[1,2], [1,1]]

ratings2 = [8,8,10,1,4,5,8,10,7,6,8,3,2,5,2,3,1,8,7,7,7,3,4,2,2,3,1,5,10,1,10,8,7,4,5,1,4,4,5,6,2,10,7,1,7]
queries2 = [[43,44], [2,36], [21,26], [37, 43]]

print(countTeams(ratings3, queries3))