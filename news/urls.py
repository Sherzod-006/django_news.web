from django.urls import path
from .views import PostListView


urlpatterns = [
    # URL pattern for the home page
    path('', PostListView.as_view(), name='home'),
]
