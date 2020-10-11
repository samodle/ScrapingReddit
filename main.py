import praw
import csv
import pandas as pd
import datetime as dt
import RedditConfig as r


def get_date(created):
    return dt.datetime.fromtimestamp(created)


# Each subreddit has five different ways of organizing the topics created by Redditors: .hot, .new, .controversial,
# .top, and .gilded. You can also use .search("SEARCH_KEYWORDS") to get only results matching an engine search.

if __name__ == '__main__':
    count = 0
    sarcastic_count = 0
    sarcastic_list = []
    for subreddit_name in r.SubReddits[:r.NumberOfSubs]:
        print('----------------------')
        print(subreddit_name + ": " + str(count) + "/" + str(len(r.SubReddits)))
        print('----------------------')
        count = count + 1
        reddit = praw.Reddit(client_id=r.APP_CLIENT_ID, client_secret=r.APP_CLIENT_SECRET, user_agent=r.APP_NAME,
                             username=r.REDDIT_USERNAME, password=r.REDDIT_PW)
        subreddit = reddit.subreddit(subreddit_name)

        target_posts = subreddit.new(limit=200)
        posts = []

        for post in target_posts:
            posts.append(
                [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

        posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
        _timestamp = posts["created"].apply(get_date)
        posts = posts.assign(timestamp=_timestamp)
        posts = posts.drop(columns=["created"])

        id_list = posts['id'].tolist()
        for id in id_list:
            submission = reddit.submission(id=id)
            submission.comments.replace_more(limit=0)
            print('Checking Comments: ' + str(len(submission.comments.list())))
            for comment in submission.comments.list():
                if "/s" in comment.body:
                    sarcastic_list += [comment.body]
                    print('Sarcastic Comment #' + str(sarcastic_count))
                    print(comment.body)
                    sarcastic_count = sarcastic_count + 1

    with open('./sarcastic.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(sarcastic_list)
    print(posts)
