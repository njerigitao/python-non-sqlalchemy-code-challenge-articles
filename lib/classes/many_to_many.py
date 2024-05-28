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