from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import urllib.request, json


def get_list_of_dict_from_soup(soup):
    main_list = []

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


class Command(BaseCommand):
    # TODO: Implement after
    args = '<foo bar ...>'
    help = 'our help string comes here, implement after'

    def _get_json_format_from_craigslist(self, query, category):
        if query is None:
            raise KeyError("Please input a query")
        else:
            query_string = query.replace(" ", "+")
            base_url = "https://toronto.craigslist.org/search/" + category + "?query=" + query_string + "&sort=rel"
            main_list = []
            soup = None
            with urllib.request.urlopen(base_url) as url:
                print(base_url)
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
        Used by our cli to handle the call/request to send to our db.
        :param category:
        :param query:
        :param args: to be implemented
        :param options: to be implemented
        :return: None
        """
        return self._get_json_format_from_craigslist(query=query, category=category)
