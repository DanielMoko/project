from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import product
from rest_framework.response import Response
from .serializers import productSerializer
from rest_framework import status
from django.http import JsonResponse

# Create your views here.
@api_view(['GET' , 'POST'])
def products(request):
    if request.method == 'GET':
        prod = product.objects.all()
        serializer = productSerializer(prod, many=True)
        return Response(serializer.data)