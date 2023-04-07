import praw
from TTS.api import TTS
import os


appID = "vbTMLYxH0FzpJJvkhX51gA"
appSecret = "N4WeNyrnvKfSFW0tEAGyBGoA68s_nw"
userAgent = "Scraper"
comments = []
titles = []
IDs = []
model_name = TTS.list_models()[0]
tts = TTS(model_name)
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
        IDs.append(submission.id)
        if f"{submission.id}.wav" in os.listdir("voice"):
            print("File already exists.")
            continue
        else:
            tts.tts_to_file(text=submission.title, speaker=tts.speakers[4], language=tts.languages[0],
                            file_path=f"voice/{submission.id}.wav")
        for i in top_comments:
            currentComment = i.body
            if "$" in i.body:
                currentComment = currentComment.replace("$", "dollar")

            tts.tts_to_file(text=i.body, speaker=tts.speakers[4], language=tts.languages[0],
                            file_path=f"voice//comments/{submission.id}_{i}.wav")
            comments.append(i.body)
