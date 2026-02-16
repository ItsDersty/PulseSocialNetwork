from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from . import settings

urlpatterns = [
    path('',views.index,name="index"),
    path('users/',include("users.urls")),
    path('posts/',include("posts.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)