from rest_framework.viewsets import ModelViewSet

from .models import CustomForm
from .serializers import CustomFormSerializer


class CustomFormViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = CustomForm.objects.all()
    serializer_class = CustomFormSerializer
