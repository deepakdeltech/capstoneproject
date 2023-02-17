from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class MenuView(APIView):
    #permission_classes = [IsAuthenticated]
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialzer = MenuSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({'status': 'successfully added',
                             'data': serialzer.data})
            

class SingleMenuItemView(APIView):
    #permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        item = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, pk):
        item = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'successfully replaced',
                             'data': serializer.data})
    
    def patch(self, request, pk):
        item = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'successfully modified',
                             'data': serializer.data})
    
    def delete(self, request, pk):
        get_object_or_404(Menu, pk=pk).delete()
        return Response({'status': 'successfully deleted'})
    
    

def index(request):
    return render(request, 'index.html', {})