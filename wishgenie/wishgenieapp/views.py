from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Wishes
from . serializers import WishSerializer
# Create your views here.


@api_view(['GET'])
def wishes(request):
    wishes = Wishes.objects.all()
    productSerializer = WishSerializer(wishes, many = True)
    return Response(productSerializer.data)