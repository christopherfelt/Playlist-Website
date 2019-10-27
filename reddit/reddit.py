import praw
import credentials

class RedditPlaylister():

    reddit = ''
    client_id = credentials.reddit_client_id
    client_secret = credentials.reddit_client_secret
    reddit_name = credentials.reddit_name


    def __init__(self):
        self.reddit = praw.Reddit(client_id = RedditPlaylister.client_id, client_secret=RedditPlaylister.client_secret, user_agent = 'me')
        self.redditor = self.reddit.redditor(name=RedditPlaylister.reddit_name)


    def getList(self, platform, subreddit):

        youtube_list = ['youtube', 'youtu.be']
        spotify_list = ['spotify']

        youtube_dict = {}
        spotify_dict = {}

        unknown_list = []
        unknown_couple = []

        youtube_count = 0
        spotify_count = 0

        in_list = False

        for submission in self.reddit.subreddit(subreddit).hot(limit=500):
            for tube in youtube_list:
                if tube in submission.url:
                    youtube_dict[submission.title] = submission.url
                    youtube_count += 1
                    in_list = True
                    break

            for spot in spotify_list:
                if spot in submission.url:
                    spotify_dict[submission.title] = submission.url
                    spotify_count += 1
                    in_list = True
                    break

            if in_list == False:
                unknown_couple.append(submission.title)
                unknown_couple.append(submission.url)
                unknown_list.append(unknown_couple)

            unknown_couple = []

        if platform.lower() == 'spotify':
            return spotify_dict
        elif platform.lower() == 'youtube':
            return youtube_dict
        else:
            return {}


def searchablesID(reddit_output):
    searchables = {}
    item_count = 0
    for key, value in reddit_output.items():
        url_parts = value.split('/')
        format_type = url_parts[3]
        format_id = url_parts[4]
        slice_number = format_id.find('?si=')
        format_id = format_id[:slice_number]
        format_collection = (format_type, format_id, value)
        searchables[key] = format_collection

        item_count +=1

        return (searchables, item_count)
