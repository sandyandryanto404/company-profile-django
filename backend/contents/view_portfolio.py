from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class Portfolio(View):
    
    @api_view(['GET'])
    def list(request):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
        
    @api_view(['GET'])
    def detail(request, id):
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': None
        }, status=status.HTTP_200_OK)
    