# Why use this scraper

Despite being slower than a headless scraper you do not need to actually log in to aquire user informations
about users who share their photos publically.
Using this vector this scraper is actually cheap on requests and thus quite stealthy.

Desirable features will be discussed in the issues shortly.

# How to use

You can use the InstagramScraper this way:

```
usage: InstagramScraper [-h] [--username USERNAME] [--level LEVEL]
                        [--destination DESTINATION]

This is the instagram scraper tool. Enjoy.

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   instagram username of the user to be scraped.
  --level LEVEL         friends level to scrape
  --destination DESTINATION
                        filename where the scraped users are to be stored.
```



# Chromedriver binary

This is the MacOSX Chromedriver binary thus it assumes you have Google Chrome installed
on a MacOSX powered machine.
For other setups in terms of os versions download the correct selenium driver for your machine
and replace the chromedriver file.
