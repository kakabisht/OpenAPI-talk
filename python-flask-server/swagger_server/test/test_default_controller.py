# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.coffee import Coffee  # noqa: E501
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


if __name__ == '__main__':
    import unittest
    unittest.main()
