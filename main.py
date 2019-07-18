import praw
import urllib.request
import time
from reddit import id, secret

reddit = praw.Reddit(
    client_id=id,
    client_secret=secret,
    user_agent="corim praw",
)

subreddit = reddit.subreddit("osugame")

limit = int(input("Please input a number of posts to parse: "))

print("Downloading images...")
start = time.time()
for submission in subreddit.hot(limit=limit):
    if "osu.ppy.sh/ss" in submission.url:
        urllib.request.urlretrieve(submission.url, "{0}.jpg".format(submission.id))
end = time.time()
print("Done! Time elapsed: {0:.4f} seconds".format(end - start))
