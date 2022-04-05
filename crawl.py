# Name: Malcolm Morton
# EUID: mtm0221
# Date: 4/5/2022
from csv import *
import csv
from xml.dom.expatbuilder import parseString
import praw

subr = input('What subreddit? Add a \'+\' between each subreddit to chain: ')

# 30 api calls per minute
# set up the reddit session with client_id, client_secret, and user_agent
reddit = praw.Reddit(client_id = 'Fk9jYcV4fnUK-PM3oH8Xeg', 
                    client_secret= '7QCk-rla-Ew9VQHGm2eTVZukgX0W-A', 
                    user_agent = 'prawcrawlerv1')

try:
    with open('Crawling_Data.csv', mode='w', encoding='utf-8') as csv_file:
        subreddit = reddit.subreddit(subr) #changes the subreddit
        keyword = input('Keyword: ')  #grab keyword
        writer = csv.writer(csv_file, delimiter='|')
        writer.writerow(['Title', 'Content'])
        for comment in subreddit.search(keyword):   # add the iteration here
            title = [comment.title, comment.selftext]
            writer.writerow(title)
            #print("Title: {}".format(comment.title))
except Exception as e:
    print(e)