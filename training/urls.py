from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_add/',views.post_add,name='post_add')

]
