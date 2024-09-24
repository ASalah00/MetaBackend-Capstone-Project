from django.contrib import admin 
from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [ 
    path('', views.sayHello, name='sayHello'), 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.bookingview.as_view(), name='booking'),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]