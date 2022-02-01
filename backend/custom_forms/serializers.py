from rest_framework.serializers import ModelSerializer
from .models import CustomForm

class CustomFormSerializer(ModelSerializer):

    class Meta:
        model = CustomForm
        fields = ['id', 'name', 'json_schema_form', 'date']