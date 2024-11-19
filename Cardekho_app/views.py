from django.shortcuts import render
from .models import Carlist,Showroomlist
from rest_framework import status
from django.http import JsonResponse,HttpResponse
from .api_file.serializers import CarSerializer,ShowroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class Showroom_view(APIView):
    
    def get(self,request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)   
        
        
class Showroom_detail(APIView):
    def get(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({'Error':'Showroom not found'},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)
        
    def put(self,request,pk):
        showroom = Showroomlist.objects.get(pk=pk)
        serializer = ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        showroom = Showroomlist.objects.get(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      

    
@api_view(['GET','POST'])
def car_list_view(request):
    if request.method == 'GET':
        try:
            car=Carlist.objects.all()
        except:
            return Response({'Error':'car not found'},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CarSerializer(car,many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','POST','DELETE'])
def car_detail_view(request,pk):
    if request.method == 'GET':    
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'POST':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
        
    if request.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    