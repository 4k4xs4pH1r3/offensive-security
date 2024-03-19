class Wappalyzer:
    def __init__(self):
        pass

    def analyze_with_categories(self, webpage: "WebPage") -> List:
        pass

class WebPage:
    def __init__(self, url: str):
        pass

    @staticmethod
    def new_from_url(url: str) -> "WebPage":
        pass
