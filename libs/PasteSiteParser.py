"""
PasteSiteParser 

This class will allow you to create a Paste Site Parsing Tool on the fly in order to generate
new paste scraping services

"""

import config
import libs.Reusables as Reusables
from libs.Clients import GetClients, GetClient
from libs.Rules import GetClientKeywordRules

import sys
import urllib3
import random
import ssl
import re
import json
from time import time, sleep


class PasteSiteParser(object):
    def __init__(self, Service=None, Pages=None, ViewAll=None, ViewPaste=None, Tag=None, TagEnd=None):
        if not Service or not Pages or not ViewAll or not ViewPaste or not Tag or not TagEnd:
            return None

        self.service = Service
        self.pages = Pages
        self.view_all = ViewAll
        self.view_paste = ViewPaste
        self.tag = Tag
        self.tag_end = TagEnd

        urllib3.disable_warnings()
        Reusables.write_log("[{0}] ##################################################################".format(
            config.APP))
        Reusables.write_log("[{0}] Beginnging {1} examination...".format(config.APP, Service))

    def begin(self):
        """
        m()

        :return:


        """
        all_links = self._get_all_links()
        for code in all_links:
            # remove sites that have the full url in the code we are parsing from the html elements
            code = code.replace('https://justpaste.it/', '')
            code = code.replace('https://pastelink.net/', '')
            code = code.replace('https://pastie.ru/view/', '')

            # filter out the website pages we typically ran into.
            # this could cause a special matching case to not parse correctly but should be okay thus far
            if "browse" not in code and "faq" not in code and "contact" not in code and \
                    "mailto" not in code and "termsandconditions" not in code and "read" not in code \
                    and "test" not in code and "about" not in code and ".php" not in code \
                    and "/lists/" not in code and "rss" not in code and "/" != code and "#" != code and \
                    'facebook' not in code and 'twitter' not in code and "/30" not in code and "/60" not in code\
                    and "trends/90" not in code and "trends/120" not in code and "trends/150" not in code \
                    and "trends/180" not in code and "trends/210" not in code and "trends/240" not in code \
                    and "trends/270" not in code and "trends/2010" not in code:

                sleeptime = random.randint(2, 10)
                sleep(sleeptime)
                url = "{}{}".format(self.view_paste, code)
                Reusables.write_log("[{0}] Parsing {1}".format(config.APP, url))
                http = urllib3.PoolManager(ssl_version=ssl.PROTOCOL_TLSv1)
                r = http.request('GET', url, headers={'User-Agent': config.USER_AGENT})
                page = r.data

                try:
                    data = page.decode("utf-8")
                except Exception as e:
                    Reusables.write_error("[{0}-ERROR] {1}".format(config.APP, e))
                    continue

                self.parse(data, code)
        return True


    def parse(self, data, code):
        """
        check()

        :param data:
        :param code:
        :return:

        Run the check that parses for the written rules inside the returned response data

        """
        """ Monitor Client Email Address """
        clients = GetClients()

        for client in clients:
            if bool(re.search(client['email'], data)):
                """ If email is found notify the clientand save an Alert Log """
                keyword = client['email']
                sms = "{0} Identified {1} at {2}{3}".format(config.APP, str(keyword), self.view_paste, code)
                url = "{}{}".format(self.view_paste, code)

                """ Logging and Notifications """
                Reusables.write_log("[{0}-ALERT] CLIENT_EMAIL: Found {1} in {2}".format(config.APP, keyword, url))
                Reusables.send_twilio_sms(client['mobile'], sms)
                Reusables.sendmail(client['email'], "SERVICE: {}\nDETAILS: {}\nURL: {}".format('Email Monitor',
                                                                                               sms, url))

        """ Monitor Client Keywords """
        client_keyword_rules= GetClientKeywordRules()

        for rule in client_keyword_rules:
            keyword = str(rule['keyword'])
            if bool(re.search(keyword, data)):
                """ If keyword is found notify the client and save an Alert Log """
                sms = "{0} Identified {1} at {2}{3}".format(config.APP, str(keyword), self.view_paste, code)
                url = "{}{}".format(self.view_paste, code)

                """ Logging and Notifications """
                client = GetClient(rule['client_id'])
                Reusables.write_log("[{0}-ALERT] : CLIENT_KEYWORD_RULE : Found {1} in {2}".format(config.APP,
                                                                                                  keyword, url))
                Reusables.send_twilio_sms(client['mobile'], sms)
                Reusables.sendmail(client['email'], "SERVICE: {}\nDETAILS: {}\nURL: {}".format('Keyword Monitor',
                                                                                               sms, url))
        return True

    def _get_all_links(self):
        """
        _get_all_links()

        :return:

        Get all links to be parsed

        """
        all_links = []
        for p in self.pages:
            url = "{}{}".format(self.view_all, p)
            http = urllib3.PoolManager(ssl_version=ssl.PROTOCOL_TLSv1)
            try:
                Reusables.write_log("[{0}] Attempting to get {1} page data.....".format(config.APP, url))
                r = http.request('GET', url, headers={'User-Agent': config.USER_AGENT})
                page = r.data
            except Exception as e:
                Reusables.write_error("[{0}] Error getting page data : {1} ".format(config.APP, e))
                Reusables.write_log("[{0}] Failed getting page, attempting next page...".format(config.APP))
                continue

            if r.data:
                Reusables.write_log("[{0}] Parsing {1} page data for URLs...".format(config.APP, url))
                while True:
                    link, page = self._get_link(page)
                    if link:
                        if ".ico".encode('utf-8') not in link \
                                and ".css".encode('utf-8') not in link \
                                and ".js".encode('utf-8') not in link \
                                and link not in all_links:

                            all_links.append(link.decode('utf-8'))
                    else:
                        break

        newlist = []
        for i in all_links:
            if i not in newlist:
                newlist.append(i)
        return newlist

    def _get_link(self, page):
        """
        _get_link(page)

        :param page:
        :return:

        Get link from between the tag and tag_end

        """
        tag = self.tag
        tag_end = self.tag_end
        tag_start = page.find(tag.encode('utf-8'))
        if not tag_start == -1:
            tag_start += len(tag)
        else:
            return None, page
        tag_end = page.find(tag_end.encode('utf-8'), tag_start)
        link = page[tag_start:tag_end]
        page = page[tag_end:]
        return link, page
