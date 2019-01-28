from . import views
from django.urls import path

app_name = 'comments'
urlpatterns = [
    path('comment/post/<int:pk>', views.post_comment, name='post_comment')
]