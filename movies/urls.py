from django.urls import path

from .views import MovieListCreateView, MovieRetriveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(), name='movies-update-delete-view'),
]