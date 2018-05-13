# Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Score: 20


def climbingLeaderboard(leaderboard, aliceScores):
    rankings = createRankings(leaderboard)
    i = len(leaderboard) - 1
    for score in aliceScores:
        flag = True
        while flag:
            if i == -1:
                print(1)
                flag = False
            elif score < leaderboard[i]:
                print(rankings[i] + 1)
                flag = False
            elif score == leaderboard[i]:
                print(rankings[i])
                flag = False
            elif score > leaderboard[i]:
                i -= 1
    return


def createRankings(leaderboard):
    rankings = [1]
    rank = 1
    for i in range(1, len(leaderboard)):
        if leaderboard[i] < leaderboard[i - 1]:
            rank += 1
        rankings.append(rank)
    return rankings


lenOfLeaderboard = int(input())
leaderboard = list(map(int, input().rstrip().split()))
lenOfAliceScores = int(input())
aliceScores = list(map(int, input().rstrip().split()))
climbingLeaderboard(leaderboard, aliceScores)
