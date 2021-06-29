from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]