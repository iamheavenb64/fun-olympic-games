from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "FunOlympics Admin Panel"
admin.site.site_title = "FunOlympics Admin Portal"
admin.site.index_title = "Welcome to FunOlympics !"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 