from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse


class TestPing(APITestCase):

    def test_ping(self):
        resp = self.client.get(reverse('ping-view'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['ping'], "PONG, BRUH")
