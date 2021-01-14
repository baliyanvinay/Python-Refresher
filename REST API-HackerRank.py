import requests


def getTotalGoals(team, year):
    total_goals = 0
    for page in range(1, 5):
        response1 = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}")
        response2 = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}")

        response1_data = response1.json()['data']
        response2_data = response2.json()['data']

        for index in range(len(response1_data)):
            total_goals += int(response1_data[index]['team1goals'])
        for index in range(len(response2_data)):
            total_goals += int(response2_data[index]['team2goals'])
    return total_goals


def getNumDraws(year):
    drawn_matches = 0
    for goal in range(6):  # Goals can be 0,1,2...
        for page in range(1, 30):
            response = requests.get(
                f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={goal}&team2goals={goal}&page={page}")
            response_data = response.json()['data']
            drawn_matches += len(response_data)
    return drawn_matches


print(getNumDraws(2011))  # 511
# getNumDraws(2011)
# print(getTotalGoals('Chelsea', 2014))
