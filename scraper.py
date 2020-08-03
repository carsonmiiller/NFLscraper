import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df
import unidecode

#for i in range(21): # to iterate through all  21 weeks of games

page = requests.get("https://www.pro-football-reference.com/years/2019/week_1.htm")
soup = BeautifulSoup(page.text, 'html.parser')

score_diff = []
week_list = soup.find_all(class_ = 'game_summary expanded nohover')
for game in week_list:
    # find differential between the score of the winner and loser, if the game wasn't a tie
    if game.find(class_ = 'winner'):
        winner_data = game.find(class_ = 'winner')
        loser_data = game.find(class_ = 'loser')
        winner_score = winner_data.find(class_ = 'right')
        loser_score = loser_data.find(class_ = 'right')
        w = int(str(winner_score.contents[0]))
        l = int(str(loser_score.contents[0]))
        diff = w - l
    # in the event of a tie, the differential is always zero
    else:
        diff = 0
    score_diff.append(diff)
print(score_diff)

