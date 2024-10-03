from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('bots_data/', views.fetch_bots_data),
    path('logout/', views.logout),
]