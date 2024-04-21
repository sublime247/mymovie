from django.contrib import admin
from watchlist.models import WatchList, StreamingPlatforms

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamingPlatforms)