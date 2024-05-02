from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.http import HttpResponse
from os.path import exists
from faker import Faker
from django.db.models import F
from contents.models import *
from django.db import connection



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
        
        results = []
        query = """
            SELECT
                a.id,
                a.title,
                a.slug,
                a.description,
                u.first_name,
                u.last_name,
                ud.about_me,
                (
                SELECT 
                        GROUP_CONCAT(r.name SEPARATOR ',') AS r 
                        FROM `references` r
                        WHERE r.id IN (
                            SELECT reference_id
                            FROM articles_references
                            WHERE article_id = a.id
                        )
                ) as categories
            FROM
                articles a
            INNER JOIN auth_user u ON u.id = a.author_id
            INNER JOIN auth_user_details ud ON ud.user_id = u.id
            WHERE
                status = 1
            ORDER BY RAND()
            LIMIT 3
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            desc = cursor.description
            results = [
                dict(zip([col[0] for col in desc], row)) 
                for row in cursor.fetchall() 
            ] 
 
        
        fake = Faker()
        data = {
            'header': {
                'title':fake.paragraph(nb_sentences=2),
                'description':fake.paragraph(nb_sentences=10)
            },
            'sliders': Slider.objects.filter(status=1).order_by("sort").values(),
            'services': Service.objects.filter(status=1).order_by("?")[:4].values(),
            'testimonial': Testimonial.objects.filter(status=1).order_by("?").values().first(),
            'articles':results
        }
        
        return Response({ 
            'status': True, 
            'message': 'ok', 
            'data': data
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