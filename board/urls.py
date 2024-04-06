from django.urls import path,include
from .views import PostList,PostDetail, PostCreate, PosttUpdate, PostDelete,index, UserPostList
from django.views.generic import TemplateView


urlpatterns = [
    path('', index),
    path('board/', PostList.as_view()),
    path('board/<int:pk>',PostDetail.as_view(),name = 'post_detail'),
    path('board/add/', PostCreate.as_view(), name = 'post_create'),
    path('board/<int:pk>/update/', PosttUpdate.as_view(), name = 'post_edit'),
    path('board/<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete'),
    path('user_posts/', UserPostList.as_view(), name='user_posts'),
    # path('replies/', reply_list, name='replies_to_user'),



]
