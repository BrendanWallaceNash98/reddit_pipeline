import praw
import sys
from praw import Reddit


def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("connected to reddit")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)


def extract_posts(reddit_isntance: Reddit, subreddit: str, time_filter:str, limit=None):
    subreddit = reddit_isntance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_lists = []

    print(posts)
