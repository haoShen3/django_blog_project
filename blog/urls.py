from django.conf.urls import url
from django.urls import path
from . import views
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('post/<int:pk>/', views.detail, name='detail'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    # path('archives/<int:year>/<int:month>', views.archives, name='archives'),
    # path('category/<int:pk>', views.category, name='category'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>', views.TagView.as_view(), name='tags'),
    # path('search/', views.search, name='search')
]