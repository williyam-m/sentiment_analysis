from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='link_index'),
    path('sentiment/', views.sentiment, name='link_sentiment')
]