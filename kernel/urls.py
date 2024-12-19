from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('hacklog/', include('hacklog.urls')),
    path('tool/', include('tools.urls'))
]
