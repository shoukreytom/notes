from django.urls import path
from account.api import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', views.create_new_user),
    path('login/', obtain_auth_token),
]