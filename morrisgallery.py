from scraper import Scraper


class MorrisGallery(Scraper):
    # http://www.wicket.space/walthamstuff?site=morris
    site = 'morris'

    def scrape(self):
        # add scraping code here
        self.add_event(self.Event(event_url="http://www.wmgallery.org.uk/event1"))