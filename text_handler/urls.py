from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_index, name='text_index'),
    path('sentiment/', views.text_sentiment, name='text_sentiment')
]