# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Order(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, customer_id: int=None, coffee_id: int=None, quantity: int=None, total_price: float=None):  # noqa: E501
        """Order - a model defined in Swagger

        :param customer_id: The customer_id of this Order.  # noqa: E501
        :type customer_id: int
        :param coffee_id: The coffee_id of this Order.  # noqa: E501
        :type coffee_id: int
        :param quantity: The quantity of this Order.  # noqa: E501
        :type quantity: int
        :param total_price: The total_price of this Order.  # noqa: E501
        :type total_price: float
        """
        self.swagger_types = {
            'customer_id': int,
            'coffee_id': int,
            'quantity': int,
            'total_price': float
        }

        self.attribute_map = {
            'customer_id': 'customerId',
            'coffee_id': 'coffeeId',
            'quantity': 'quantity',
            'total_price': 'totalPrice'
        }
        self._customer_id = customer_id
        self._coffee_id = coffee_id
        self._quantity = quantity
        self._total_price = total_price

    @classmethod
    def from_dict(cls, dikt) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Order of this Order.  # noqa: E501
        :rtype: Order
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self) -> int:
        """Gets the customer_id of this Order.


        :return: The customer_id of this Order.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: int):
        """Sets the customer_id of this Order.


        :param customer_id: The customer_id of this Order.
        :type customer_id: int
        """

        self._customer_id = customer_id

    @property
    def coffee_id(self) -> int:
        """Gets the coffee_id of this Order.


        :return: The coffee_id of this Order.
        :rtype: int
        """
        return self._coffee_id

    @coffee_id.setter
    def coffee_id(self, coffee_id: int):
        """Sets the coffee_id of this Order.


        :param coffee_id: The coffee_id of this Order.
        :type coffee_id: int
        """

        self._coffee_id = coffee_id

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Order.


        :return: The quantity of this Order.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Order.


        :param quantity: The quantity of this Order.
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def total_price(self) -> float:
        """Gets the total_price of this Order.


        :return: The total_price of this Order.
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price: float):
        """Sets the total_price of this Order.


        :param total_price: The total_price of this Order.
        :type total_price: float
        """

        self._total_price = total_price