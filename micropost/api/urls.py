from django import views
from django.urls import path
import views


urlpatterns = [
    path("users/<username>/collection", views.MicropostListView.as_view(), 
         name="user-collection"),
    path("users/<username>/collection/<pk>", views.MicropostView.as_view(), 
         name="micropost-detail")
]