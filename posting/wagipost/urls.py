from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.post_list),
    path('api/posts/<int:post_id>/', views.post_detail),
]
