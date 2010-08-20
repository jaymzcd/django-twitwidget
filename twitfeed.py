
import urllib
import urllib2

def twitter_search(query, limit=10):
    import simplejson as json
    """
        returns a list of results based on a
        query using the public twitter api -
        no rate limits and no api keys needed
    """
    query = urllib.quote(query)
    req = ("http://search.twitter.com/search.json?q=%s") % query
    data = json.loads(urllib2.urlopen(req).read())
    text_results = []
    for item in data['results']:
        text_results.append(item['text'])
    return text_results[:limit]

def twitter_usertimeline(user, limit=10):
    from BeautifulSoup import BeautifulSoup
    """
        returns the user timeline tweets by parsing the page. likely
        to cause trouble - ratelimit/api calls instead perhaps? :)
    """
    req = ("http://twitter.com/%s") % user
    data = (urllib2.urlopen(req).read())
    soup = BeautifulSoup(data)
    tweets = []
    for tweet in soup.html.body.findAll('span', {'class':'entry-content'}):
        # q&d check to get rid of rt/at's
        #if (tweet.contents[0][:1] != '@' and tweet.contents[0][:2] != 'RT'):
        tweets.append(tweet.contents[0])
    return tweets[:limit]

