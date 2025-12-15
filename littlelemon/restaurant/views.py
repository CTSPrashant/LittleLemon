from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Menu
from .serializers import MenuSerializer, BookinSerializer

def sayHello(request):
 return HttpResponse('Hello World')
# Create your views here.

def index(request):
    return render(request, 'index.html', {})



# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookinSerializer