
import tweepy, re, twitterKeys, tag


RE_EMOJI = re.compile(
    u'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])')
TWEET_COUNT = 500
PAGE_COUNT = TWEET_COUNT / 100
DIV_BY = 4

auth = tweepy.OAuthHandler(twitterKeys.consumer_key, twitterKeys.consumer_secret)
auth.set_access_token(twitterKeys.access_token, twitterKeys.access_token_secret)

api = tweepy.API(auth)


unRepeatedList = []
LATEST_ID = 0


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001F900-\U0001F9FF"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def appendToList(newString):
    unRepeatedList.append(newString)


def cleanDuplicatedTweets(resultObject, array, string):
    global LATEST_ID
    if (string not in array):
        appendToList(string)
        LATEST_ID = resultObject.id


def cleantext(resultObject):
    newString = ' '.join(re.sub(r'(\#[A-Za-z0-9ğüşöçİĞÜŞÖÇ]*)(?!;)', '', resultObject.full_text).split())  # cleans Hashtags
    newString = ' '.join(re.sub(r'((RT)*( )*\@[a-zA-Z0-9ğüşöçİĞÜŞÖÇ_]*:?)(?!;)', '', newString).split())  # cleans RT
    newString = remove_emoji(newString)  # cleans Emoji
    newString = ' '.join(re.sub(r'(https:\/\/[a-zA-Z0-9.\/]*\b)', '', newString).split())  # cleans links
    cleanDuplicatedTweets(resultObject, unRepeatedList, newString)

counter = 0
while (counter<TWEET_COUNT):
    public_tweets = api.search(q='edirne', tweet_mode='extended', count=TWEET_COUNT, max_id = LATEST_ID)
    for tweetIndex in range(len(public_tweets)):
        cleantext(public_tweets[tweetIndex])
    for tweet in unRepeatedList:
        print(tweet)
        tag.twitArray(tweet)
#
# tag.twitArray('recep tayyip erdoğan blabalba nabtin i̇stanbul')
