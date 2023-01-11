from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /movies/1/
    path('<int:movie_id>/', views.detail, name='detail')
]