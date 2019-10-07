"""

Rules

"""

def GetClientKeywordRules():
    """
    GetClientKeywordRules()

    :return:

    Returns client_keyword_rules

    This function can be modified to return your client email rules from a MySQL database

    [{CLIENT_ID, KEYWORD}]
    """
    client_keyword_rules = [
        [0, "randomword"]
    ]

    return client_keyword_rules