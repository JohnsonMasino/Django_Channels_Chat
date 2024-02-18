from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # the url for the admin site
    path('', include('chat.urls')), # the url for the chat app
    path('notifications/', include('notifications.urls')), # the url for the notifications app
]
