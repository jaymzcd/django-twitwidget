from django.db import models

class TwitterWidget(models.Model):
    INTERVAL_CHOICES = (
        (6000, '6s'),
        (10000, '10s'),
        (30000, '30s'),
        (60000, '1 minute'),
    )
    BEHAVIOUR_CHOICES = (
        ('all', 'Show set # of tweets'),
        ('default', 'Stream in tweets'),
    )

    # Core & behaviour
    username = models.CharField(max_length=50)
    behaviour = models.CharField(max_length=10, choices=BEHAVIOUR_CHOICES)
    update_interval = models.IntegerField(choices=INTERVAL_CHOICES, default=6000)
    tweets_to_show = models.IntegerField(default=5)
    url = models.CharField(max_length=200, default='/')
    url.help_text = 'The URL that this widget should appear for'

    # Look & feel attrs
    widget_width = models.IntegerField(default=250)
    widget_height = models.IntegerField(default=300)
    use_autowidth = models.BooleanField(default=False)
    use_autowidth.help_text = 'When enabled width will be overridden and the widget expand to fit'
    shell_background = models.CharField(max_length=6, default='333333')
    shell_color = models.CharField(max_length=6, default='ffffff')
    tweets_background = models.CharField(max_length=6, default='000000')
    tweets_color = models.CharField(max_length=6, default='000000')
    tweets_links = models.CharField(max_length=6, default='4aed05')

    # Options for widget
    show_scrollbar = models.BooleanField(default=False)
    show_avatars = models.BooleanField(default=False)
    show_hashtags = models.BooleanField(default=False)
    show_timestamps = models.BooleanField(default=False)
    loop_results = models.BooleanField(default=False)
    poll_data = models.BooleanField(default=True)
    poll_data.help_text = 'When enabled tweets will feed in automagically'

    def __unicdode__(self):
        return '%s (%s)' % (self.username, self.url)
