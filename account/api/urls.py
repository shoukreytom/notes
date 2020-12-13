from django.urls import path
from account.api import views


urlpatterns = [
    path('register/', views.create_new_user),
]