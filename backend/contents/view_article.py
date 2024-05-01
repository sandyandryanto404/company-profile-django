from django.views import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 

class Article(View):
    
    @api_view(['GET'])
    def list(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def detail(request, slug):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def comment_list(request, id):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def comment_create(request, id):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
    