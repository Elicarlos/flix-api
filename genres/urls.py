from django.urls import path
from .views import GenreCreateListView, GenreRetriverUpdateDeleteView


urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name="genre-create-list"),
    path('genres/<int:pk>/', GenreRetriverUpdateDeleteView.as_view(), name="genre-detail-view"),
]