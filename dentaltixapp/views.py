"""Module for view sets"""
from dentaltixapp.models import ProgrammingLanguage
from dentaltixapp.serializers import ProgrammingLanguageSerializer
from rest_framework import viewsets
from django.http import HttpResponse
import json
from rest_framework import status


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    """Class for programming_language's view sets """
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer
    lookup_field = 'name'

    def create(self, request, *args, **kwargs):
        """redefine create because it gives problem.
        When frameworks doesn't exist and I add allow_null=True in serializer... Django
        """
        programming_language = json.loads(request.body)
        if 'frameworks' not in request.data:
            programming_language['frameworks'] = []
        serialized_language = ProgrammingLanguageSerializer(data=programming_language)
        status_to_response = status.HTTP_400_BAD_REQUEST
        if serialized_language.is_valid():
            serialized_language.save()
            status_to_response = status.HTTP_201_CREATED
            response = serialized_language.data
        else:
            response = serialized_language.errors
        return HttpResponse(json.dumps(response), status=status_to_response, content_type='application/json')
