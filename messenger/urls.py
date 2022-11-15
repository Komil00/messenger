from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from messenger import settings

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('customusers.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/', include('rest_framework.urls')),
    path('swagger/', schema_view),
    path('', include('correspondence.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
