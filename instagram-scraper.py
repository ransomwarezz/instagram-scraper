import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


def isUserLink(link):
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


driver = webdriver.Chrome('./chromedriver')

username = "<Enter Username here>"
userLink = "https://www.instagram.com/" + username + "/"


def scrapeUser(userLink):
    driver.get(userLink)
    links = driver.find_elements_by_tag_name('a')
    users = []

    safetyCounter = 0
    for link in links:

        try:
            linkAdress = link.get_attribute("href")
        except StaleElementReferenceException:
            links = driver.find_elements_by_tag_name('a')[:safetyCounter]
            continue

        if "taken-by" in linkAdress:
            # print linkAdress
            link.click()

            time.sleep(3)
            potentialUsers = driver.find_elements_by_tag_name('a')
            if potentialUsers is not None:
                for potentialUser in potentialUsers:

                    if potentialUser.get_attribute('href') is not None and potentialUser.get_attribute(
                            'title') in potentialUser.get_attribute('href'):
                        parent = potentialUser.find_element_by_xpath('..')

                        if isUserLink(potentialUser):
                            users.append(potentialUser.get_attribute('href'))

                potentialCloseButtons = driver.find_elements_by_tag_name('button')

                for potentialCloseButton in potentialCloseButtons:
                    if 'CLOSE' in potentialCloseButton.text.upper():
                        potentialCloseButton.click()
        safetyCounter += 1
    return set(users)


def scrapeMultipleLevels(userLink, levels=1, previousList=set(), finalList=[]):
    if levels == 0:
        return finalList
    users = scrapeUser(userLink)
    finalList.extend(users)
    # Prevent endless loop
    users.discard(userLink)
    for oldUser in previousList:
        users.discard(oldUser)
    for link in users:
        # print link
        finalList.extend(scrapeMultipleLevels(link, levels - 1, users))

    return finalList


allUsers = list(set(scrapeMultipleLevels(userLink)))
# Uncomment for complete list
print allUsers
driver.close()
