class Article:
    def __init__(self, title, urlImage, author, url, date):
        self.title = title
        self.urlImage = urlImage
        self.author = author
        self.url = url
        self.date = date

class New:
    """
    News Class to define news objects
    """
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

