from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name="index"),
    path('new/', views.PostCreateView.as_view(), name="new"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="show"),
]
