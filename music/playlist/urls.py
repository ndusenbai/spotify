from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.choose, name='choose'),
    path('playlist/', views.playlist, name='playlist'),
    path('song/', views.song, name='song'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
