from django.contrib import admin
from django.urls import path, include
from .views import AllPastesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AllPastesView.as_view(), name='homepage'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('pastes/', include('pastes.urls')),
]
