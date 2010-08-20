from django.contrib import admin
from twitterstuff.models import TwitterWidget

class WidgetAdmin(admin.ModelAdmin):
    list_display = ('username', 'url', 'behaviour')

admin.site.register(TwitterWidget, WidgetAdmin)
