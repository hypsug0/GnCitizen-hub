from rest_framework.serializers import ModelSerializer, SlugRelatedField

from commons.models import Tags
from commons.serializers import TagsSerializer

from .models import CustomForm


class CustomFormSerializer(ModelSerializer):
    tags = TagsSerializer(many=True)
    # tags = SlugRelatedField(many=True, read_only=True, slug_field="source")

    class Meta:
        model = CustomForm
        fields = ["id", "name", "json_schema_form", "date", "tags"]

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        custom_form = CustomForm.objects.create(**validated_data)
        for t in tags:
            print(t)
            custom_form.tags.get_or_create(label=t["label"])
        return custom_form
