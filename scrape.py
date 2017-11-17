# Flask server method - FYI only to show how it works


import importlib
import inspect
import sys
from pprint import pprint

# @app.route('/walthamstuff')
# def getScrapedStuff():
#     #http://www.wicket.space/walthamstuff?site=sitename
#     site = request.args.get('site')
#     scraper = scrape.get_scrapers()
#     scraped_site = scraper[site]()
#     return jsonify({'data': scraped_site.results})
from scrapers.millE17 import MillE17
from scrapers.morrisgallery import MorrisGallery


def get_scrapers():
    """Provides the service with a dict of available scraper classes
    and the required value (site) to call each - No need to edit """
    cls_members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    scraper_dict = {}
    for cls in cls_members:
        scraper_dict[cls[1].site] = cls[1]
    return scraper_dict


def print_scrapers():
    scrapers = get_scrapers()
    for scraper in scrapers:
        scraper_name = scrapers[scraper].__name__
        this_scraper = getattr(importlib.import_module("scrape"), scraper_name)
        instance = this_scraper()
        pprint(instance.results)


###############################################################################################################
# EXAMPLE SCRAPER CLASSES

class Morris(MorrisGallery):
    pass


class Mill(MillE17):
    pass


if __name__ == "__main__":
    # m = MillE17()
    # print(pprint(m.results))
    pprint(print_scrapers())
