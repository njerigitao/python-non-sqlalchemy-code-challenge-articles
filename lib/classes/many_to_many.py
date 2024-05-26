class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        pass

    def article_titles(self):
        return[article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article,author