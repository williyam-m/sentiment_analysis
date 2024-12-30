from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='text_index'),
    path('sentiment/', views.sentiment, name='text_sentiment')
]