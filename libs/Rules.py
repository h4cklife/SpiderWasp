"""

Rules

"""

def GetClientKeywordRules():
    """
    GetClientKeywordRules()

    :return:

    Returns client_keyword_rules

    This function can be modified to return your client keyword rules from a MySQL database

    Using mysql.connector v2+ you can return a dict.
        See: https://stackoverflow.com/questions/22769873/python-mysql-connector-dictcursor

    [{"client_id": 0, "keyword": "randomword"}]
    
    """
    client_keyword_rules = [
        {"client_id": 0, "keyword": "randomword"}
    ]

    return client_keyword_rules