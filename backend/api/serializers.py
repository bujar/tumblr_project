from rest_framework import serializers
from api.models import TumblrCache


class TumblrCacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = TumblrCache
        fields = ('tumblr_name',
                  'json_response')