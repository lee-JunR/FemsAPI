from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kwh/', include('kwh.urls')),
    path('temp/', include('temp.urls')),
]
