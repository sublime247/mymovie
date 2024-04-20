from django.urls import path, include
from watchlist.api.views import movie_lst, movie_detail

urlpatterns = [
    path('list/', movie_lst, name='movie-lst'),
    path('<int:pk>', movie_detail, name='movie-detail')
]
