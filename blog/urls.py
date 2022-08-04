from django.urls import path
from .views import Bloglistview

app_name='blog'

urlpatterns = [
    path('', Bloglistview.as_view, name='home')
]
