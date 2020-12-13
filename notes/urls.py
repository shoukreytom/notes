from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    # api
    path('notes/api/v1/notes/', include('home.api.urls')),
]
