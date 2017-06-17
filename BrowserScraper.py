import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


class BrowserScraper():
    def __init__(self, username, level, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome('./chromedriver')
        pass

    def wait(self):
        time.sleep(3)

    def scrapeUser(self, userLink):
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
                link.click()
                self.wait()
                potentialUsers = self.driver.find_elements_by_tag_name('a')
                if potentialUsers is not None:
                    for potentialUser in potentialUsers:

                        if potentialUser.get_attribute('href') is not None and potentialUser.get_attribute(
                                'title') in potentialUser.get_attribute('href') and BrowserScraper.isUserLink(
                            potentialUser):
                            users.append(potentialUser.get_attribute('href'))

                    potentialCloseButtons = self.driver.find_elements_by_tag_name('button')

                    for potentialCloseButton in potentialCloseButtons:
                        if 'CLOSE' in potentialCloseButton.text.upper():
                            potentialCloseButton.click()
            safetyCounter += 1
        return set(users)

    @classmethod
    def getUserLink(cls, username):
        return "https://www.instagram.com/" + username + "/"

    @classmethod
    def isUserLink(cls, link):
        address = link.get_attribute('href')
        parent = link.find_element_by_xpath('..')

        return "/accounts/" not in address and \
               "/p/" not in address and \
               "/legal/" not in address and \
               'LI' in parent.get_property("tagName").upper() and \
               '/blog.instagram.com/' not in address and \
               '/about/' not in address and \
               '/explore/' not in address and \
               '/developer/' not in address and \
               'instagram-press.com' not in address and \
               'help.instagram.com' not in address
