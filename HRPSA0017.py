#Solution for "Climbing the leaderboard" 
#Link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    player_ranks = []

    i = len(ranked) -1
    for score in player:
        while i >= 0 and score >= ranked[i]:
            i -= 1
        if i == -1:
            player_ranks.append(1)
        else:
            player_ranks.append(i + 2)

    return player_ranks


NnumPlayer=int(input())
scores=input()
scoresArr=list(map(int,scores.split()))
MnumGames=int(input())
playerScores=input()
playerScoresArr=list(map(int,playerScores.split()))
result=climbingLeaderboard(scoresArr,playerScoresArr)
for i in range(0,len(result)):
    print(result[i])


#Alternative way (using Pandas library)

import pandas as pd

def climbingLeaderboard(ranked, player):
    # Create a DataFrame for ranked scores
    df_ranked = pd.DataFrame(ranked, columns=['Score'])
    
    # Remove duplicate scores and reindex
    df_ranked = df_ranked['Score'].drop_duplicates().reset_index(drop=True)

    # Create a DataFrame for player scores
    df_player = pd.DataFrame(player, columns=['Score'])

    # Add a new column for dense rank to the ranked DataFrame
    df_ranked['Rank'] = df_ranked['Score'].rank(method='dense', ascending=False)

    # Iterate through player scores
    for i in range(len(df_player)):
        score = df_player.loc[i, 'Score']

        # Find the rank for the player's score using the ranked DataFrame
        rank = df_ranked[df_ranked['Score'] >= score]['Rank'].min()

        # If the player's score is higher than all on the leaderboard
        if pd.isna(rank):
            rank = len(df_ranked) + 1

        print(int(rank))


NnumPlayer = int(input())
scores = input()
scoresArr = list(map(int, scores.split()))
MnumGames = int(input())
playerScores = input()
playerScoresArr = list(map(int, playerScores.split()))
climbingLeaderboard(scoresArr, playerScoresArr)
