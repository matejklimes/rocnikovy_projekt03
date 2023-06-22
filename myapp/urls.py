from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('developers/', views.DeveloperListView.as_view(), name='developers_list'),
    path('developers/<int:pk>/', views.DeveloperDetailView.as_view(), name='developer_detail'),
    path('games/', views.GameListView.as_view(), name='games_list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('games/add/', views.GameCreateView.as_view(), name='game_add'),
]
