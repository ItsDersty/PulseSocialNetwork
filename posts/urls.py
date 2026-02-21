from django.urls import path, include
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('new/', views.newPost, name='newPost'),
    path('<int:id>',views.viewPost,name="postPage"),
]