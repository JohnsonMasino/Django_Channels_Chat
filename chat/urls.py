from django.urls import path
from .views import Page

urlpatterns = [
    path('', Page, name='chat_page'),
]