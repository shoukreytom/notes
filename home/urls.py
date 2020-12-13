from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.NoteList.as_view(), name='notes'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('notes/create/', views.CreateNote.as_view(), name='create-note'),
    path('notes/<int:pk>/update/', views.UpdateNote.as_view(), name='update-note'),
    path('notes/<int:pk>/delete/', views.DeleteNote.as_view(), name='delete-note'),
]