import json
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

import argparse

from BrowserScraper import BrowserScraper


def main():
    parser = argparse.ArgumentParser(prog="InstagramScraper", description='This is the instagram scraper tool. Enjoy.')
    parser.add_argument('--username', dest='username', help='instagram username of the user to be scraped.')
    parser.add_argument('--level', dest='level', help='friends level to scrape', default=1)
    parser.add_argument('--destination', dest='destination', help='filename where the scraped users are to be stored.',
                        default='scraped.json')
    arguments = parser.parse_args()

    scraper = BrowserScraper(arguments.username, arguments.level)
    allUsers = scraper.scrape()
    destination = arguments.destination
    if not destination.lower().endswith(".json"):
        destination += ".json"
    with open(destination, mode='w') as destinationFile:
        json.dump(allUsers, destinationFile)

    # print allUsers
    # print scraper.images
    scraper.closeDriver()


if __name__ == '__main__':
    main()
