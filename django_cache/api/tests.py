from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse

class CachedEndpointViewTestCase(APITestCase):

    def setUp(self):
        super(CachedEndpointViewTestCase, self).setUp()
        self.api_endpoint = reverse('api:cached')

    def test_api_endpoint_should_be_cached_for_get_requests(self):

        response = self.client.get(self.api_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cached_response = self.client.get(self.api_endpoint)
        self.assertEqual(response.data['served_at'], cached_response.data['served_at'])


    def test_api_endpoint_should_not_be_cached_for_post_requests(self):

        response = self.client.post(self.api_endpoint, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cached_response = self.client.post(self.api_endpoint, {})
        self.assertNotEqual(response.data['served_at'], cached_response.data['served_at'])


class NonCachedEndpointViewTestCase(APITestCase):

    def setUp(self):
        super(NonCachedEndpointViewTestCase, self).setUp()
        self.api_endpoint = reverse('api:not_cached')

    def test_api_endpoint_should_not_be_cached(self):

        response = self.client.get(self.api_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cached_response = self.client.get(self.api_endpoint)
        self.assertNotEqual(response.data['served_at'], cached_response.data['served_at'])



