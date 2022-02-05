from api.models import Bookmark
from api.serializers import BookmarkSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models import Q


class BookmarkListCreate(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(Q(owner=user) | Q(private=False))
        else:
            bookmark = Bookmark.objects.filter(private=False)
        return bookmark

    def perform_create(self, serializer):
        serializer.save(self.request.user)


class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(owner=user)

    def perform_update(self, serializer):
        serializer.save(self.request.user)
