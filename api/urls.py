from django.urls import path
from api.views import BookmarkListCreate, BookmarkDetail

urlpatterns = [
    path('bookmark/', BookmarkListCreate.as_view()),
    path('bookmark/<int:pk>/', BookmarkDetail.as_view()),
]
