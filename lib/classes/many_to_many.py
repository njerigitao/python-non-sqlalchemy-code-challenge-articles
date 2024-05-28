class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

        @property
        def name(self):
            return self._name
        def articles(self):
            return self._articles
        def add_article(self, magazine, title):
            if not isinstance(magazine, Magazine):
                raise TypeError("Magazine must be an instance of Magazine")
            if not isinstance(title, str):
                raise TypeError("Title must be a string")
            if len(title) < 5 or len(title) > 50:
                raise ValueError("Title must be between 5 and 50 characters")
            article = Article(self, magazine, title)
            self._articles.append(article)
            return article
        def magazines(self):
            return list(set([article.magazine for article in self._articles]))
        def topic_areas(self):
            magazines = self.magazines()
            if not magazines:
                return None
            return list(set([magazine.category for magazine in magazines]))
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        