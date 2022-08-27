import praw
import time

from configparser import ConfigParser
from Quote_summon import SummonQuote

sq = SummonQuote()
config = ConfigParser()
botname = "BB-Quotes-Bot"
filename = 'BB-Quotes-Bot\Data/response_data.json'

config.read('BB-Quotes-Bot\Data\BotData.ini')

reddit = praw.Reddit(
    client_id=config['main']['client_id'],
    client_secret=config['main']['client_secret'],
    password=config['main']['password'],
    user_agent=config['main']['user_agent'],
    username=config['main']['username']
)


# Main Loop
while True:

    # Goes through each mention of the bot.
    for mention_id in reddit.inbox.mentions(limit=10):
        time.sleep(5)
        mention_id = str(mention_id)

        # "mention" is a class and is not iterable
        mention = reddit.comment(mention_id)
        mention.refresh()
        replies = mention.replies

        # Goes through the replies of the mention.
        for reply in replies:
            author = reply.author

            # Break if there is a reply by the bot
            if reply.author == botname:
                break
        else:
            quote = sq.create_random_quote()
            # print(quote)
            mention.reply(body=quote)
            time.sleep(30)
