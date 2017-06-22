class Scraper():
    @classmethod
    def getUserLink(cls, username):
        return "/".join(["https://www.instagram.com", username] )+ "/"

    @classmethod
    def isUserLink(cls, address,title):

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