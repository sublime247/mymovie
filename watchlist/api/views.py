from watchlist.models import WatchList, StreamingPlatforms
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework import status

# <<<<<class base view>>>>

class StreamPlatformAV(APIView):
    def get(self, request):
        stream = StreamingPlatforms.objects.all()
        streamSterializer = StreamPlatformSerializer(stream, many=True)
        return Response(streamSterializer.data)
    
    
    def post(self, request):
        stream = StreamPlatformSerializer(data=request.data)
        if stream.is_valid():
            stream.save()
            return Response(stream.data)
        else:
            return Response(stream.error)
        
class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        stream= StreamingPlatforms.objects.get(pk=pk)
        streamSterializer = StreamPlatformSerializer(stream)
        return Response(streamSterializer.data)     
            
    def put(self, request, pk):
        stream= StreamingPlatforms.objects.get(pk=pk)
        streamSterializer= StreamPlatformSerializer(stream, data=request.data)
        if streamSterializer.is_valid():
            streamSterializer.save()
            return Response(streamSterializer.data)
        else:
            return Response(streamSterializer.error)
    def delete(self, request, pk):
        stream= StreamingPlatforms.objects.get(pk=pk)
        stream.delete()
        return Response()




class WatchListAV(APIView):
        # for get request
    def get(self, request):
        WatchLists = WatchList.objects.all()
        data = WatchListSerializer(WatchLists, many=True)
        return Response(data.data)
    def post(self, request):
        data = WatchListSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)


class WatchListDetailAv(APIView):
    def get(self, request, pk):
            WatchListDetail = WatchList.objects.get(pk=pk)
            detail = WatchListSerializer(WatchListDetail)
            return Response(detail.data)
        
    def put(self, request, pk):
            WatchList = WatchList.objects.get(pk=pk)
            data= WatchListSerializer(WatchList,data=request.data)
            if data.is_valid():
                data.save()
                return Response(data.data)
            else:
                return Response(data.errors)
    def delete(self, request, pk):
         WatchList = WatchList.objects.get(pk=pk)
         WatchList.delete()
         return Response()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # <<<<<function base view below>>>>

# @api_view(['GET', 'POST'])
# def WatchList_lst(request):
#     if request.method=='GET':
#         WatchLists = WatchList.objects.all()
#         data = WatchListSerializer(WatchLists, many=True)
#         return Response(data.data)
    
#     if request.method=="POST":
#         data = WatchListSerializer(data=request.data)
#         if data.is_valid():
#             data.save()
#             return Response(data.data)
#         else:
#             return Response(data.errors)



# @api_view(['GET', 'PUT', 'DELETE'])
# def WatchList_detail(request, pk):
#     if request.method=='GET':
#         WatchListDetail = WatchList.objects.get(pk=pk)
#         detail = WatchListSerializer(WatchListDetail)
#         return Response(detail.data)
    
#     if request.method=='PUT':
#         WatchList = WatchList.objects.get(pk=pk)
#         data= WatchListSerializer(WatchList,data=request.data)
#         if data.is_valid():
#             data.save()
#             return Response(data.data)
#         else:
#             return Response(data.errors)
        
#     if request.method=='DELETE':
#          WatchList = WatchList.objects.get(pk=pk)
#          WatchList.delete()
#          return Response()
        
    