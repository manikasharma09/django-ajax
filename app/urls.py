from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('index',views.index,name='index'),
    path('likepost',views.likePost,name='likepost'),
]
