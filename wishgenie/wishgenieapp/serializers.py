from rest_framework import serializers
from . models import Wishes

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishes
        fields = "__all__"