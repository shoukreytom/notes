from django.urls import path
from home.api import views


urlpatterns = [
    path('', views.NoteListApiView.as_view()),
    path('<int:pk>/', views.NoteDetailApiView.as_view()),
    path('<int:pk>/update/', views.update_note_api),
    path('<int:pk>/delete/', views.delete_note_api),
    path('create/', views.create_note_api),
]