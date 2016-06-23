"""Module for Tests"""
from rest_framework import status
from rest_framework.test import APITestCase
from dentaltixapp.models import ProgrammingLanguage, Framework
from django.core.exceptions import ObjectDoesNotExist


class AccountTests(APITestCase):
    def test_create_programming_language_without_frameworks(self):
        data = {'name': 'test'}
        response = self.client.post('/programminglanguage/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProgrammingLanguage.objects.count(), 1)
        self.assertEqual(ProgrammingLanguage.objects.get().name, 'test')
        with self.assertRaises(ObjectDoesNotExist):
            Framework.objects.get().name

    def test_create_programming_language_with_frameworks(self):
        data = {'name': 'test', 'frameworks': ['1']}
        response = self.client.post('/programminglanguage/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProgrammingLanguage.objects.count(), 1)
        self.assertEqual(ProgrammingLanguage.objects.get().name, 'test')
        self.assertEqual(Framework.objects.get().name, '1')

    def test_create_programming_language_with_2_frameworks(self):
        data = {'name': 'test', 'frameworks': ['1', '2']}
        response = self.client.post('/programminglanguage/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProgrammingLanguage.objects.count(), 1)
        self.assertEqual(ProgrammingLanguage.objects.get().name, 'test')
        self.assertEqual(Framework.objects.get(name='1').name, '1')
        self.assertEqual(Framework.objects.get(name='2').name, '2')

    def test_create_programming_language_and_exists(self):
        data = {'name': 'test'}
        response = self.client.post('/programminglanguage/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {'name': 'test'}
        response = self.client.post('/programminglanguage/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)