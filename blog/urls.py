from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug>/remove/', views.post_remove, name='post_remove'),
    path('post/<slug:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
