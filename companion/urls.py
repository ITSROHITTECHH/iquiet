from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('chat.html', views.chat),
    path('chat-api/', views.chat_api),
]


