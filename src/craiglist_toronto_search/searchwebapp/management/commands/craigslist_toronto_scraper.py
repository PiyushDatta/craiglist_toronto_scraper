"""
Class that does the magic of getting json formatted list from craigs list.
We keep this under a Command class because it is better django practice
as you can now call this through manage.py. We can also use this to
create a command line interface later on.
"""

import urllib.request

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


def get_list_of_dict_from_soup(soup):
    """
    This function goes through the soup element to find the relevant
    tags for our json output.

    :param soup: BeautifulSoup4 element
    :return: List[{dict}]
    """
    main_list = []

    if soup:
        for node in soup.find_all('p', attrs={'class': 'result-info'}):
            title = "Not given"
            price = "Not given"
            date = "Not given"

            if node.find('a', attrs={'class': 'result-title hdrlnk'}):
                title = node.find('a', attrs={'class': 'result-title hdrlnk'}).get_text()

            if node.find('span', attrs={'class': 'result-price'}):
                price = node.find('span', attrs={'class': 'result-price'}).get_text()

            if node.find('time'):
                date = node.find('time')['title']

            node_dict = {
                "title": title,
                "date": date,
                "price": price
            }
            main_list.append(node_dict)
        return main_list
    else:
        raise TypeError("Please enter a valid BeautifulSoup element")


class Command(BaseCommand):
    # TODO: Implement after
    args = '<foo bar ...>'
    help = 'our help string comes here, implement after'

    @staticmethod
    def _get_json_format_from_craigslist(query, category):
        """
        Takes in query and category and creates a connection to craigslist toronto
        in order to get the html code. It then formats it with BeautifulSoup4, which
        we then scrape for tags to get our relevant info.
        :param query: String
        :param category: String
        :return: List[{dict}]
        """
        if query is None:
            raise KeyError("Please input a query")
        else:
            query_string = query.replace(" ", "+")
            base_url = "https://toronto.craigslist.org/search/" + category + "?query=" + query_string + "&sort=rel"
            with urllib.request.urlopen(base_url) as url:
                soup = BeautifulSoup(url, 'html.parser')
                if not soup:
                    raise ConnectionError("Could not fetch from craigslist")
                else:
                    json_format_list = get_list_of_dict_from_soup(soup)
                    return json_format_list

    # TODO: Implement after
    def _flush_all_points(self):
        pass

    def handle(self, query, category='sss', *args, **options):
        """
        Used by our cli to handle the call/request to process.
        :param query: String
        :param category: String
        :param args: to be implemented
        :param options: to be implemented
        :return: List[{dict}]
        """
        return self._get_json_format_from_craigslist(query=query, category=category)
