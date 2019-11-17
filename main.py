import tweepy,re,twitterKeys

RE_EMOJI = re.compile(u'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])')

auth = tweepy.OAuthHandler(twitterKeys.consumer_key, twitterKeys.consumer_secret)
auth.set_access_token(twitterKeys.access_token, twitterKeys.access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search(q='Edirne', count=1000, tweet_mode='extended')

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

def cleantext(text):
    newString = ' '.join(re.sub(r'((RT)*( )*\@[a-zA-Z0-9ğüşöçİĞÜŞÖÇ_]*:?)(?!;)', '', text).split()) # cleans RT
    newString = ' '.join(re.sub(r'(\#[A-Za-z0-9ğüşöçİĞÜŞÖÇ]*)(?!;)', '', newString).split()) # cleans Hashtags
    newString = remove_emoji(newString) # cleans Emoji
    newString = ' '.join(re.sub(r'(https:\/\/[a-zA-Z0-9.\/]*\b)', '', newString).split()) # cleans mention
    return newString


for tweet in public_tweets :
    print(cleantext(tweet.full_text))




