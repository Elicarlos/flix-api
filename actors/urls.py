from django.urls import path

from .views import ActorCreateListView, ActorRetriveUpdateDelete

urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='actors'),
    path('actors/<int:pk>/', ActorRetriveUpdateDelete.as_view(), name='actor-update-delete-view'),
]