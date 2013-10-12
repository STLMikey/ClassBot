import time
import pprint
import praw

r = praw.Reddit('classbot for rhockey_dev')
already_done = []

badwords = ['class ', 'classy ', 'classless', ' class']

subreddit = r.get_subreddit('hockey')
subreddit_comments = subreddit.get_comments(limit=100000)
for comment in subreddit_comments:
	has_class = any(string in comment.body for string in badwords)
	if has_class:
		print comment.body
		print '################';
