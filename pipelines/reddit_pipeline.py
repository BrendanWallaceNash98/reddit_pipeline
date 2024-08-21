from etl.reddit_etl import connect_reddit, extract_posts
from utils.constants import CLIENT_ID, SECRET


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    posts = extract_posts(instance, subreddit, time_filter, limit)