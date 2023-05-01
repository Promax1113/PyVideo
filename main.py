import praw
from TTS.api import TTS
import os
import screenshot
import videomakertest
import discord
from idSaver import *

web = discord.SyncWebhook.from_url("https://discord.com/api/webhooks/1093996610033295501" +
                                   "/oAIcATKPu7Q_9DhY47slY7_WhRevvJM_WfIHZL3y_wJ-bc6uuIhFn3DwjIc2SjWcorU7")
subreddit_name = "AskReddit"

appID = "Insert Your App ID"
appSecret = "Insert Your Secret"
userAgent = "Insert Your UserAgent"
comments = []
titles = []
IDs = []
commentIDs = []
URLs = []
baseUrl = "https://old.reddit.com"
model_name = TTS.list_models()[0]
tts = TTS(model_name)
reddit = praw.Reddit(client_id=appID, client_secret=appSecret, user_agent=userAgent)
screenshots_dir = "scr"
tries = 0
screen_width, screen_height = 400, 800

submissions = reddit.subreddit(subreddit_name).top(time_filter="week", limit=3)

for submission in submissions:
    if submission.over_18:
        print("Submission was 18+")
        continue
    else:
        tries += 1
        submission.comment_sort = 'best'
        top_comments = submission.comments[:3]
        print(submission.title)
        titles.append(submission.title)

        # if submission.id == read_id(submission.id)[0]:
        #     print(f"{read_id(submission.id)[1]} is already in file list.")
        #     submissions.append(reddit.subreddit(subreddit_name).top(time_filter="week", limit=4)[tries + 1])

        # else:
        IDs.append(submission.id)
        # save_id(submission.id, submission.title)
        currentUrl = baseUrl + submission.permalink
        print(f"Link: {currentUrl}")
        URLs.append(currentUrl)
        screenshot.get_post_scr(currentUrl, submission.id)
        tts.tts_to_file(text=submission.title, speaker=tts.speakers[4], language=tts.languages[0],
                        file_path=f"voice/{submission.id}.wav")

    for comment in top_comments:
        currentComment = comment.body
        commentIDs.append(comment.id)
        if len(currentComment) > 500:
            print("Comment was more than 500 chars. Skipping...")
            pass
        else:
            if "$" in comment.body:
                currentComment = currentComment.replace("$", "dollar")
            tts.tts_to_file(text=currentComment, speaker=tts.speakers[4], language=tts.languages[0],
                            file_path=f"voice//comments/{submission.id}_{comment}.wav")
            comments.append(comment.body)

# for url in URLs:
#     screenshot.get_comment_screenshot(url, IDs[URLs.index(url)])
#     web.send(f"Screenshots done for {url}!!!")

for ID in IDs:
    videomakertest.make_movie(ID, commentIDs[IDs.index(ID)])
    web.send("Finished 1 video!")

web.send("Finished!!")
