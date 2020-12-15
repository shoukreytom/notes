from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('account.urls')),

    # api
    path('notes/api/v1/', include('home.api.urls')),
    path('accounts/api/v1/', include('account.api.urls'))
]
