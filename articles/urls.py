from django.urls import path, include
from articles import views

urlpatterns = [
    path("", views.articleAPI.as_view(), name="index"),
    path("<int:article_id>/", views.article_detailAPI.as_view(), name="article_view"),
]
