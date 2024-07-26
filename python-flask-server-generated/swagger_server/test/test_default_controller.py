# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.coffee import Coffee  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.order_response import OrderResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_coffees_get(self):
        """Test case for coffees_get

        Get a list of all available coffees
        """
        response = self.client.open(
            '/v1/coffees',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_coffees_id_get(self):
        """Test case for coffees_id_get

        Get details of a specific coffee
        """
        response = self.client.open(
            '/v1/coffees/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_id_get(self):
        """Test case for orders_id_get

        Get details of a specific order
        """
        response = self.client.open(
            '/v1/orders/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_post(self):
        """Test case for orders_post

        Place a new order
        """
        body = Order()
        response = self.client.open(
            '/v1/orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
