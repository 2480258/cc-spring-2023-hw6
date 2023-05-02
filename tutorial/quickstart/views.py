from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view

lst = []
@api_view(['GET', 'POST'])
def get_list(request):
    if request.method == 'GET':
        return JsonResponse(lst, safe=False)
        # 'safe=False' for objects serialization
    if request.method == 'POST':
        lst.append(request.data)
        return JsonResponse(lst, safe=False)
 

