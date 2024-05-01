from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.http import HttpResponse
from os.path import exists

class Page(View):
    
    @api_view(['GET'])
    def ping(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def home(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def about(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def service(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def faq(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def contact(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['POST'])
    def message(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['POST'])
    def subscribe(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def download(request, path):

        path_upload = settings.DJANGO_UPLOAD_PATH
        file_path = str(path_upload)+"/"+str(path)

        file_exists = exists(file_path)
        if(file_exists == False):
            return Response({ 'status': False, 'message': "File not found in directory!", 'data': None }, status=status.HTTP_400_BAD_REQUEST)

        image_data  = open(file_path, 'rb').read()
        return HttpResponse(image_data, content_type="image/png")