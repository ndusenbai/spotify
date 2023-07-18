from django.urls import include, path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update, name='update'),
    path('register/', views.register, name='register'),
]
