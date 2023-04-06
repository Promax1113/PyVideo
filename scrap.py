import sys
import praw
import subprocess


appID = "vbTMLYxH0FzpJJvkhX51gA"
appSecret = "N4WeNyrnvKfSFW0tEAGyBGoA68s_nw"
userAgent = "Scraper"
comments = []
titles = []

reddit = praw.Reddit(client_id=appID, client_secret=appSecret, user_agent=userAgent)

for submission in reddit.subreddit("AskReddit").top(time_filter="week", limit=3):
    if submission.over_18:
        print("Submission was 18+")
        continue
    else:
        submission.comment_sort = 'best'
        top_comments = submission.comments[:3]
        print(submission.title)
        titles.append(submission.title)
        print(titles)
        for comment in top_comments:
            comments.append(comment)

if len(titles) == 2:
    title1 = titles[0]
    title2 = titles[1]
    title3 = " "
elif len(titles) == 3:
    title1 = titles[0]
    title2 = titles[1]
    title3 = titles[2]
elif len(titles) == 1:
    title1 = titles[0]
    title2 = ""
    title3 = ""

subprocess.Popen([sys.executable, 'voiceover.py'] + comments, title1, title2, title3)
