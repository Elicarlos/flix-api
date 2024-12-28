from django.urls import path

from .views import ReviewListCreateView, ReviewRetriveUpdateDestroy


urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews'),
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroy.as_view(), name='review-update-delete-view')
]