from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer
    