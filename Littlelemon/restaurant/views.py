from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking,Menu
from .serializers import bookSerializer,menuSerializer,UserSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth.models import User
def sayHello(request):
 return render(request,'index.html',{})

class bookingview(APIView):
 def get(self,request):
  items=Booking.objects.all()
  serializer=bookSerializer(items,many=True)
  return Response(serializer.data)#returnJSON
 def post(self,request):
  serializer=bookSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({"status":"success","data":serializer.data})
  
class MenuItemsView(generics.ListCreateAPIView):#get and post  requests
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):#get put, delete  requests
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Fetch all Booking objects
    serializer_class = bookSerializer  # Use the BookingSerializer



@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})