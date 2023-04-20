from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer 
# Create your views here.
@api_view()
def myapp(request):
    return Response({'status':200, 'message': 'Welcome to My Project'})

