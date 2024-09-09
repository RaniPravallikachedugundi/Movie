from django.urls import path
from . import views
urlpatterns=[
    path('<int:pk>/',views.about_movie,name='about_movie'),
]