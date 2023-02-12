#!/usr/bin/python
# -*- coding: utf-8 -*-
"""GeoNature-Citizen hub commons serializers
"""


from rest_framework.serializers import ModelSerializer

from .models import Tags


class TagsSerializer(ModelSerializer):
    """Tags serializer"""

    class Meta:  # pylint: disable=too-few-public-methods
        """TagsSerializer Meta class"""

        model = Tags
        fields = ["label"]
