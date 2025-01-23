from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    path('manga/list', views.manga_list, name='manga_list'),  
    path('manga/<int:id>/', views.manga_detail, name='manga_detail'),
    path('manga/<int:id>/favorite/', views.favorite_manga, name='favorite_manga'),
    path('manga/<int:id>/unfavorite/', views.unfavorite_manga, name='unfavorite_manga'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    
]
