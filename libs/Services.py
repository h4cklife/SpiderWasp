"""

service, pages, viewall, viewpaste, tag, tag_end

"""
def GetServices():
    """
    GetServices()

    :return:

    List of services to parse.
    Dead/no longer parsable services have been commented out in case they come live again.

    [SERVICE_NAME, PAGES_TO_GET_URLS_FROM, VIEW_ALL_PASTES_URL, VIEW_A_PASTE_URL, START_TAG, TAG_END]

    """
    services = [
        ['Slexy', ['/slexy/recent'], "https://slexy.org", "https://slexy.org/view/", '<a href="/view/', '"'],
        # DEAD ['Justpasteit', ['/top', '/top/day/new'], "https://justpaste.it", "https://justpaste.it", "<a href='", "'"],
        # DEAD "['Lpaste', ['/browse?pastes_page=1'], "http://lpaste.net", "http://lpaste.net/raw/", '<a href="/', '"'],
        # JS/JQ ['Pastefs', ['/recent.php', '/trends.php'], "https://www.pastefs.com", "https://www.pastefs.com/pid/",
        # 'href="https://www.pastefs.com/pid/', '"'],
        ['Pastelink', ['/read'], "https://pastelink.net", "https://pastelink.net/", '<a href="', '"'],
        # DEAD ['Pasteonline', ['/archive.php'], "https://pasteonline.org", "https://pasteonline.org", '<a href="', '"'],
        ['Pasteorgru', ['/'], "http://paste.org.ru", "http://paste.org.ru/?", "<a href=\'/?", "\'"],
        ['Pastie', ['/lists', '/trends'], "https://pastie.ru", "https://pastie.ru/view/", '<a href="', '"']
    ]

    return services