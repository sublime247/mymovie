from django.urls import path, include
from watchlist.api.views import MovieList, MovieDetail

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-lst'),
    path('<int:pk>', MovieDetail.as_view(), name='movie-detail')
]
