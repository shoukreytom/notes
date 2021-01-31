from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('account.urls')),

    # api
    path('accounts/', include('rest_framework.urls')),
    path('api/v1/notes/', include('home.api.urls')),
    path('api/v1/accounts/', include('account.api.urls')),
    path('api/v1/doc/', schema_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
