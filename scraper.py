from collections import namedtuple


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
