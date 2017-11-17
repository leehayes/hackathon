import importlib
import inspect
import sys
from collections import namedtuple
from pprint import pprint


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


class Scraper:
    """The parent class from which all site scraper classes can
    inherit in order to serialise the API's json output"""

    # Event fields required to be returned from scraping - TBC
    Event = namedtuple('Event', ['site', 'description', 'datetime', 'event_url', 'img_urls'])
    Event.__new__.__defaults__ = (None,) * len(Event._fields)

    # http://www.wicket.space/walthamstuff?site=demo
    site = 'demo'

    def __init__(self):
        self.events = []
        self.scrape()

    def add_event(self, event):
        event = event._replace(site=self.site)
        self.events.append(event)

    def scrape(self):
        # Add an event
        self.add_event(self.Event(site="this will be replaced with self.site",
                                  description='Exciting stuff is planned!',
                                  datetime='yyyy-mm-ddThh:mm:ss.000Z',
                                  event_url='www.demosite.com/events/exciting',
                                  img_urls=['www.123.com/123.jpg', 'www.xx.com/xx.jpg']))
        # Add another event......
        self.add_event(self.Event(description="Leaving out lots of details. No field is mandatory"))

    @property
    def results(self):
        if self.events:
            return self.events
        else:
            return "No Events Found"


###############################################################################################################
# EXAMPLE SCRAPER CLASSES

# @app.route('/walthamstuff')
# def getScrapedStuff():
#     #http://www.wicket.space/walthamstuff?site=sitename
#     site = request.args.get('site')
#     scraper = scrape.get_scrapers()
#     scraped_site = scraper[site]()
#     return jsonify({'data': scraped_site.results})

class AllScrapers(Scraper):
    site = 'all'
    print_scrapers()


class MorrisGallery(Scraper):
    # http://www.wicket.space/walthamstuff?site=morris
    site = 'morris'

    def scrape(self):
        # add scraping code here
        self.add_event(self.Event(event_url="http://www.wmgallery.org.uk/event1"))


class MillE17(Scraper):
    # http://www.wicket.space/walthamstuff?site=mill
    site = 'mill'

    def scrape(self):
        # add scraping code here
        self.add_event(self.Event(event_url="http://themille17.org/event1",
                                  description="Stuff Happens"))
        self.add_event(self.Event(event_url="http://themille17.org/event2",
                                  description="More Stuff Happens"))


if __name__ == "__main__":
    # m = MillE17()
    # print(pprint(m.results))
    # pprint(print_scrapers())
    pprint(AllScrapers().results)
