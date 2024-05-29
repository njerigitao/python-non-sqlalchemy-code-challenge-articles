class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

        @property
        def author(self):
            return self._author
        
        @property
        def magazine(self):
            return self._magazine

        @property
        def title(self):
            return self._title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Author name must be a string")
        self.name = name
        self._articles = []

        @property
        def name(self):
            return self.__name

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
        if not isinstance(name, str):
            raise ValueError("Magazine name must be a string")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self.name = name
        self.category = category
        self._articles = []

        @property
        def name(self):
            return self.__name
        @property
        def category(self):
            return self.__category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return[article.title for article in self._articles]

    def contributing_authors(self):
       pass

        