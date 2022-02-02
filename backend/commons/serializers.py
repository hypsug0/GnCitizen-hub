from rest_framework.serializers import ModelSerializer

from .models import Tags


class TagsSerializer(ModelSerializer):

    class Meta:
        model=Tags
        fields=['label']