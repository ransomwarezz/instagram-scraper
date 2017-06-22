class Scraper():
    @classmethod
    def getUserLink(cls, username):
        return "/".join(["https://www.instagram.com", username] )+ "/"

