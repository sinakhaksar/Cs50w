from django.urls import path
from . import views


urlpatterns =[
    path("", views.index, name="index"),
    path("sina", views.sina, name='sina'),
    path("zari", views.zh, name="zahra"),
    path("<str:name>",views.greet, name="greet-all")
]

