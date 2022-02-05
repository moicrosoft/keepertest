from api.models import Bookmark
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'created_at' , 'private']

    def save(self, user, *args, **kwargs):
        if user.is_authenticated:
            kwargs["owner"] = user
        super(BookmarkSerializer, self).save(*args, **kwargs)
    