from django.urls import path,include
from .views import PostList,PostDetail, PostCreate, PosttUpdate, PostDelete
from django.views.generic import TemplateView


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>',PostDetail.as_view(),name = 'post_detail'),
    path('add/', PostCreate.as_view(), name = 'post_create'),
    path('<int:pk>/update/', PosttUpdate.as_view(), name = 'post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete')


]
