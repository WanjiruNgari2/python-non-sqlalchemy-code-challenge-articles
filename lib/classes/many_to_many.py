class Article:
    all = []

    def __init__(self, author, magazine, title=""):
        self._author = self.check_author(author)
        self._magazine = self.check_magazine(magazine)
        self._title = self.check_title(title)
        Article.all.append(self)

    def check_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters long")
        return title

    def check_author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        return author

    def check_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        return magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = self.check_author(value)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = self.check_magazine(value)

class Author:
    all = []

    def __init__(self, name):
        self._name = self.check_name(name)
        Author.all.append(self)

    def check_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        return name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    def __init__(self, name, category):
        self._name = self.property_name(name)
        self._category = self.property_category(category)

    def property_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters long")
        return name

    def property_category(self, category):
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        return category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self.property_name(value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = self.property_category(value)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len([article for article in self.articles() if article.author == author]) > 2]
        if not authors:
            return None
        return authors