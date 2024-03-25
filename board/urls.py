from django.urls import path,include
from .views import PostList,PostDetail
from django.views.generic import TemplateView


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>',PostDetail.as_view(),name = 'post_detail'),


]
