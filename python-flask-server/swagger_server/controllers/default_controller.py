import connexion
import six

from swagger_server.models.coffee import Coffee  # noqa: E501
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
