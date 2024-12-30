from django.urls import path
from . import views

urlpatterns = [
    path('', views.link_index, name='link_index'),
    path('sentiment/', views.link_sentiment, name='link_sentiment')
]