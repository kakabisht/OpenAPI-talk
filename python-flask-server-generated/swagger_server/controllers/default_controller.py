import connexion
import six

from swagger_server.models.coffee import Coffee  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.order_response import OrderResponse  # noqa: E501
from swagger_server import util


def coffees_get():  # noqa: E501
    """Get a list of all available coffees

    Returns a list of all coffees available in the shop. # noqa: E501


    :rtype: List[Coffee]
    """
    return 'do some magic!'


def coffees_id_get(id):  # noqa: E501
    """Get details of a specific coffee

    Returns details of a coffee given its ID. # noqa: E501

    :param id: ID of the coffee
    :type id: int

    :rtype: Coffee
    """
    return 'do some magic!'


def orders_id_get(id):  # noqa: E501
    """Get details of a specific order

    Returns details of an order given its ID. # noqa: E501

    :param id: ID of the order
    :type id: int

    :rtype: OrderResponse
    """
    return 'do some magic!'


def orders_post(body):  # noqa: E501
    """Place a new order

    Creates a new coffee order. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: OrderResponse
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
