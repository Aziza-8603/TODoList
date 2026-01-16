from django.contrib import admin
from django.urls import path, include
from tasks.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    path('users/', include('users.urls')),
    path('', include('tasks.urls')),
]


