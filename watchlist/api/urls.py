from django.urls import path, include
from watchlist.api.views import WatchListAV, WatchListDetailAv, StreamPlatformAV,StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-lst'),
    path('list/<int:pk>', WatchListDetailAv.as_view(), name='movie-detail'),
    
    
    path('streams/', StreamPlatformAV.as_view(), name= 'streams'),
    path('streams/<int:pk>', StreamPlatformDetailAV.as_view(), name= 'stream-details'),
]
