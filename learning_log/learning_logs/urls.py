"""define URL patterns for learning_logs
import the path function which is needed when mapping URLs to views.
import the view module, the dot tells python to import the view.py module from the same directory as the current urls.py module.


"""

from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('topics/',views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
