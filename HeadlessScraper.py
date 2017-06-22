import mechanize

from DictUtils import listToDict
from Scraper import Scraper
import pprint

prettyPrinter = pprint.PrettyPrinter(indent=4,width=50)


class HeadlessScraper():
    def __init__(self, username):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.baseUrl = "https://www.instagram.com"
        self.username = username
        self.userLink = Scraper.getUserLink(username)

    def scrapeUser(self, userLink=None):
        if userLink is None:
            userLink = self.userLink
        response = self.browser.open(userLink)
        text = response.read()
        allUserLinks = {}
        for link in self.browser.links(url_regex='/p/'):
            self.browser.follow_link(link)
            userLinks = [link for link in self.browser.links()
                         if HeadlessScraper.isUserLink(link) and
                         self.isNotCurrentUserLink(link, userLink)
                         ]
            userLinksDict = listToDict(lambda userLink: Scraper.getUserLink(userLink.text), userLinks)
            allUserLinks.update(userLinksDict)

        return allUserLinks

    def isNotCurrentUserLink(self, link, userLink):
        return link.url.strip() not in userLink.strip()

    @classmethod
    def isUserLink(cls, link):
        address = link.url
        titles = [(key, value) for key, value in link.attrs if key.lower() == 'title']

        if len(titles) == 0:
            return False

        _, title = titles.pop()

        return address is not None and \
               title in address and \
               "/accounts/" not in address and \
               "/p/" not in address and \
               "/legal/" not in address and \
               '/blog.instagram.com/' not in address and \
               '/about/' not in address and \
               '/explore/' not in address and \
               '/developer/' not in address and \
               'instagram-press.com' not in address and \
               'help.instagram.com' not in address


prettyPrinter.pprint(HeadlessScraper('pipapo').scrapeUser())
