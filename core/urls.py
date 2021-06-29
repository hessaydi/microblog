# from django.conf.urls import path, include
# from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.contrib import admin

# from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.views import get_swagger_view

# swagger documentation
# schema_swagger_view = get_swagger_view(title='Recipes API')
# coreapi documentation
# schema_view = get_schema_view(title="Recipes API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('api.urls')),
    # rest_framework urls for session authentication for the browsable api
    # path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('api_docs/', schema_swagger_view),
    # path('docs/', include_docs_urls(title='Recipes API')),
    # path('schema', schema_view),
]