
from django.urls import path,include
from .views import HomeView,PostDetailView, AddPostView, PostUpdateView, PostDeleteView,BlogCategoryView, LikeView
urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
  path('add_post/', AddPostView.as_view(), name='add_post'),
  path('post/edit/<int:pk>', PostUpdateView.as_view(), name='update_post'),
  path('post/<int:pk>/remove', PostDeleteView.as_view(), name='delete_post'),
  path('blogcategory/<str:bcats>', BlogCategoryView, name='blog_category'),
  path('like/<int:pk>', LikeView, name='like_post'),

]