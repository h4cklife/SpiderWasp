"""

Clients

"""

def GetClients():
    """
    GetClients()

    :return:

    Returns clients

    This function can be modified to return your clients and email rules from a MySQL database

    [{CLIENT ID, FULL NAME, MOBILE, ERMAIL}]

    """
    clients = [
        {"client_id": 0, "full_name": "John Doe", "mobile": "12223334444", "email": "example@gmail.com"},
    ]

    return clients

def GetClient(id):
    """
    GetClient(id)
    :param id:
    :return:

    Notes:  Could use pandas for better performance
            https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search

    """
    for client in GetClients():
        if client['client_id'] == id:
            return client
