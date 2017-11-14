#Flask server method - FYI only to show how it works
# @app.route('/walthamstuff')
# def getScrapedStuff():
#     #http://www.wicket.space/walthamstuff?site=sitename
#     site = request.args.get('site')
#     scraper = scrape.get_scrapers()
#     scraped_site = scraper[site]()
#     return jsonify({'data': scraped_site.results})

import sys, inspect
from collections import namedtuple

def get_scrapers():
    """Provides the service with a dict of available scraper classes
    and the required value (site) to call each - No need to edit """
    cls_members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    scraper_dict = {}
    for cls in cls_members:
        scraper_dict[cls[1].site] = cls[1]
    return scraper_dict


class Scraper:
    """The parent class from which all site scraper classes can
    inherit in order to serialise the API's json output"""

    #Event fields required to be returned from scraping - TBC
    Event = namedtuple('Event', ['site', 'description', 'datetime', 'event_url', 'img_urls'])
    Event.__new__.__defaults__ = (None,) * len(Event._fields)

    #http://www.wicket.space/walthamstuff?site=demo
    site = 'demo'

    def __init__(self):
        self.events = []
        self.scrape()

    def add_event(self, event):
        event = event._replace(site=self.site)
        self.events.append(event)

    def scrape(self):
        #Add an event
        self.add_event(self.Event(site="this will be replaced with self.site",
                            description='Exciting stuff is planned!',
                            datetime='YYYYMMDD HH:MM',
                            event_url='www.demosite.com/events/exciting',
                            img_urls=['www.123.com/123.jpg', 'www.xx.com/xx.jpg']))
        #Add another event......
        self.add_event(self.Event(description="Leaving out lots of details. No field is mandatory"))

    @property
    def results(self):
        if self.events:
            return self.events
        else:
            return "No Events Found"

###############################################################################################################
#EXAMPLE SCRAPER CLASSES

class Morris(Scraper):
    #http://www.wicket.space/walthamstuff?site=morris
    site = 'morris'
    def scrape(self):
        self.add_event(self.Event(event_url="http://www.wmgallery.org.uk/event1"))

class Mill(Scraper):
    #http://www.wicket.space/walthamstuff?site=mill
    site = 'mill'
    def scrape(self):
        self.add_event(self.Event(event_url="http://themille17.org/event1",
                                    description="Stuff Happens"))
        self.add_event(self.Event(event_url="http://themille17.org/event2",
                                    description="More Stuff Happens"))

