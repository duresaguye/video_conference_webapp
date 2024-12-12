from django.urls import path
from . import views

urlpatterns = [ 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('video-call/<str:room_name>/', views.video_call, name='video_call_with_room'),
    path('video-call/', views.video_call, name='video_call'),
]