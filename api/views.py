from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import string
import random

# Create your views here.
# def get_random_string(size):
#     return ''.join(random.choice(string.ascii_letters) for _ in range(size))

@api_view(["GET","POST"])
def get_random_string(request, length):
    try:
        if (length<5001):
            random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        else:
            random_string = "Error: Requested string length out of bounds! Please enter in the range (1-5000)"
        return JsonResponse(random_string, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)