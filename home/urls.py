from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('challenge/', views.challenge, name='challenge'),
    path('challenge/<int:id>', views.challenge, name='challenge_id'),
]
