# from django.shortcuts import render
# from watchlist.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_lst(request):
#     movies = Movie.objects.all()
#     data = {"movies":list(movies.values())}
#     print(data)
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movieDetail = Movie.objects.get(pk=pk)
#     data = {
#         "name":movieDetail.name,
#         "description":movieDetail.description,
#         "isActive":movieDetail.isActive
        
#     }
#     return JsonResponse(data)