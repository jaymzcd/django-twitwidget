from django import template
from twitterstuff.twitfeed import twitter_search, twitter_usertimeline
from twitterstuff.models import TwitterWidget

register = template.Library()

@register.inclusion_tag('feed.html')
def twitter_feed(qry, result_limit=10):
    data = twitter_search(qry, result_limit)
    return {'data' : data}

@register.inclusion_tag('feed.html')
def twitter_user(user, result_limit=10):
    data = twitter_usertimeline(user, result_limit)
    return {'data' : data}

@register.inclusion_tag('widget.html')
def render_widget(source_url='/'):
    try:
        widget = TwitterWidget.objects.get(url=source_url)
    except TwitterWidget.DoesNotExist:
        widget = None
    return {'widget': widget}
