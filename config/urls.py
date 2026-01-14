from django.contrib import admin
from django.urls import path, include
from tasks.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    path('users/', include('users.urls')),
    path('', include('tasks.urls')),
]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('tasks.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
