from scrapers.scraper import Scraper


class MillE17(Scraper):
    # http://www.wicket.space/walthamstuff?site=mill
    site = 'mill'

    def scrape(self):
        # add scraping code here
        self.add_event(self.Event(event_url="http://themille17.org/event1",
                                  description="Stuff Happens"))
        self.add_event(self.Event(event_url="http://themille17.org/event2",
                                  description="More Stuff Happens"))