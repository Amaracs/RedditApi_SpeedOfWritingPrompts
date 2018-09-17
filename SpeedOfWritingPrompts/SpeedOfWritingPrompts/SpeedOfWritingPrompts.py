#Import Reddit API
import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='-',
                     client_secret='-',
                     user_agent='my user agent')



reddit.read_only  
subreddit = reddit.subreddit('writingprompts')



