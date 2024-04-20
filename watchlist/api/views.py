from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def movie_lst(request):
    if request.method=='GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True)
        return Response(data.data)
    
    if request.method=="POST":
        data = MovieSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method=='GET':
        movieDetail = Movie.objects.get(pk=pk)
        detail = MovieSerializer(movieDetail)
        return Response(detail.data)
    
    if request.method=='PUT':
        movie = Movie.objects.get(pk=pk)
        data= MovieSerializer(movie,data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
    if request.method=='DELETE':
         movie = Movie.objects.get(pk=pk)
         movie.delete()
         return Response()
        
    