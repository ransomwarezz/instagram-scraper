import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Scraper import Scraper


class BrowserScraper():
    def __init__(self, username, linkLevel, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome('./chromedriver')

        self.username = username
        self.usernameLink = Scraper.getUserLink(username)
        self._linkLevel = self.linkLevel = linkLevel
        self.images = {}

    def reset(self):
        self.linkLevel = self._linkLevel

    def wait(self):
        # TODO: Add selenium way of waiting
        time.sleep(1.5)

    def scrapeUser(self, userLink, levels):
        self.driver.get(userLink)
        links = self.driver.find_elements_by_tag_name('a')
        users = []

        safetyCounter = 0
        for link in links:

            try:
                linkAdress = link.get_attribute("href")
            except StaleElementReferenceException:
                links = self.driver.find_elements_by_tag_name('a')[:safetyCounter]
                continue

            if "taken-by" in linkAdress:
                try:
                    self.images[levels].append(linkAdress)
                except Exception:
                    self.images[levels] = []
                    self.images[levels].append(linkAdress)

                link.click()
                self.wait()
                potentialUsers = self.driver.find_elements_by_css_selector('li > a')

                if potentialUsers is None:
                    potentialUsers = []

                for user in [user for user in potentialUsers if BrowserScraper.isUserLink(user)]:
                    # print  user.get_attribute('href')
                    users.append(user.get_attribute('href'))

                potentialCloseButtons = self.driver.find_elements_by_tag_name('button')

                for potentialCloseButton in potentialCloseButtons:
                    if 'CLOSE' in potentialCloseButton.text.upper():
                        potentialCloseButton.click()
            safetyCounter += 1
        return set(users)

    def scrapeMultipleLevels(self, userLink, levels=1, previousList=set(), finalList=[]):
        if levels == 0:
            return finalList
        users = self.scrapeUser(userLink, levels)
        finalList.extend(users)
        # Prevent endless loop
        users.discard(userLink)
        for oldUser in previousList:
            users.discard(oldUser)
        for link in users:
            # print link
            finalList.extend(self.scrapeMultipleLevels(link, levels - 1, users))
        self.closeDriver()
        return finalList

    def scrape(self, levels=1, previousList=set(), finalList=[]):
        return list(set(self.scrapeMultipleLevels(self.usernameLink, levels, previousList, finalList)))

    def closeDriver(self):
        self.driver.close()

    @classmethod
    def isUserLink(cls, link):
        address, title = cls.extractAdressAndTitle(link)
        parent = cls.extractParent(link)

        return Scraper.isUserLink(address, title) and\
               'LI' in parent.get_property("tagName").upper()

    @classmethod
    def extractParent(cls, link):
        parent = link.find_element_by_xpath('..')
        return parent

    @classmethod
    def extractAdressAndTitle(cls, link):
        address = link.get_attribute('href')
        title = link.get_attribute('title')
        return address, title
