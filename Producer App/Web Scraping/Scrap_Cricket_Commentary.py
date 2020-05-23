import urllib.request as urllib2
import pandas as pd
from bs4 import BeautifulSoup
import os

directory = os.getcwd()

if os.path.exists('Scores.csv'):
        scores_df = pd.read_csv('Scores.csv')
else:
        scores_df = pd.DataFrame(columns=['ball', 'score', 'commentary'])        




for filename in os.listdir(directory+'/Data/'):
        if filename.endswith(".html"):
                ball_df = pd.DataFrame(columns=['ball', 'score', 'commentary'])
                
                # create empty lists for each of the data you want
                ball_numbers = list()
                ball_score = list()
                ball_desc = list()
                
                with open(filename,encoding='utf-8') as fp:
                        innings_soup = BeautifulSoup(fp, "html5lib")

                for div in innings_soup.findAll('div', {'class': 'time-stamp'}):
                        ball_numbers.append(div.text)

                # for score on each ball
                for div in innings_soup.findAll('div', {'class': 'over-circle'}):
                        if (div.text.strip()) == 'W':
                                ball_score.append('7')
                        else:
                                if len(div.text.strip()) == 1:
                                        ball_score.append(div.text)
                                else:
                                        t_val = []
                                        for val in div.text.strip():
                                
                                                if val.isalpha():
                                                        pass
                                                else:
                                                        t_val.append(val)
                        
                                        ball_score.append(''.join(x for x in t_val))
        


        # for description of each ball
                for div in innings_soup.findAll('div', {'class': 'description'}):
                        ball_desc.append(div.text)

    # save lists in respective dataframe columns
                ball_df.ball = ball_numbers
                ball_df.score = ball_score
                ball_df.commentary = ball_desc

                scores_df = pd.concat([scores_df,ball_df], ignore_index=True)

scores_df.to_csv("Scores.csv", sep=',', index=False)