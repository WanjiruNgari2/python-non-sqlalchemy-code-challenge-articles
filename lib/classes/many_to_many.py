class Article:
    all = [] # empty list of all articles

    def __init__(self, author, magazine, title=""):
        self._author = self.check_author(author)
        self._magazine = self.check_magazine(magazine)
        self._title = self.check_title(title)
        Article.all.append(self) # add articles to the class variable all

    def check_title(self, title):
        if not isinstance(title, str): # check that the title is a string
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50): #  check that the title is between 5 and 50 characters long
            raise ValueError("Title must be between 5 and 50 characters long")
        return title

    def check_author(self, author):
        if not isinstance(author, Author): # check that the author is an instance of Author class
            raise ValueError("Author must be of type Author") # raise an error if the author is not an instance of Author class
        return author

    def check_magazine(self, magazine):
        if not isinstance(magazine, Magazine): # check that the magazine is an instance of Magazine class
            raise ValueError("Magazine must be of type Magazine") # raise an error if the magazine is not an instance of Magazine class
        return magazine

    @property # property decorator for title
    def title(self): 
        return self._title  # this will return the title 

    @title.setter # setter decorator for title that will raise an error if user is trying to change the title
    def title(self, value):
        raise AttributeError("Title is immutable")

    @property # property decorator for author that will return the author
    def author(self):
        return self._author

    @author.setter 
    def author(self, value):
        self._author = self.check_author(value) # checks if the author is an instance of Author class and checks if it's not the same as the current author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = self.check_magazine(value)

class Author:
    all = [] # empty list of all authors

    def __init__(self, name):
        self._name = self.check_name(name) 
        Author.all.append(self) # add authors to the class variable all as soon as they are created

    def check_name(self, name):
        if not isinstance(name, str): # check that the name is a string
            raise ValueError("Name must be a string")
        if len(name) == 0: # check that the name of the author is not empty
            raise ValueError("Name must be longer than 0 characters")
        return name

    @property # property decorator for name that will return the name
    def name(self):
        return self._name

    @name.setter # setter decorator for name that will raise an error if user is trying to change the name
    def name(self, value):
        raise AttributeError("Name is immutable")

    def articles(self):
        return [article for article in Article.all if article.author == self] # return all articles written by the author

    def magazines(self):
        return list(set(article.magazine for article in self.articles())) # return all magazines published by the author

    def add_article(self, magazine, title):
        return Article(self, magazine, title) # will create and add a new article with the author, magazine and title

    def topic_areas(self):
        if not self.articles():
            return None
            # use set to remove duplicates and return all unique articles published by the author in a list of tuples (magazine, title)
        return list(set(article.magazine.category for article in self.articles())) # return all unique categories of magazines published by the author

class Magazine:
    all = [] # empty list of all magazines

    def __init__(self, name, category):
        self._name = self.property_name(name)
        self._category = self.property_category(category)
        Magazine.all.append(self) # add magazines to the class variable all as soon as they are created

    def property_name(self, name):
        if not isinstance(name, str): # check that the name is a string
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16): # check that the name of the magazine is between 2 and 16 characters long
            raise ValueError("Name must be between 2 and 16 characters long")
        return name

    def property_category(self, category):
        if not isinstance(category, str): # check that the category is a string
            raise ValueError("Category must be a string")
        if len(category) == 0: # check that the category of the magazine is not empty
            raise ValueError("Category must be longer than 0 characters")
        return category

  # use property decorators for name and category that will return the name and category
    @property
    def name(self):
        return self._name

    @name.setter # setter will basically return the name if it's not changed by the user
    def name(self, value):
        self._name = self.property_name(value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value): 
        self._category = self.property_category(value)

    def articles(self):
        # return all articles published by the magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
            # return all authors who have contributed to the magazine, use set to remove duplicates and return all unique authors
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles(): # return None if there are no articles published by the magazine
            return None
        return [article.title for article in self.articles()] # return all unique titles of articles published by the magazine

    def contributing_authors(self): # return all authors who have contributed to the magazine with more than 2 articles published
        authors = [author for author in self.contributors() if len([article for article in self.articles() if article.author == author]) > 2]
        if not authors:
            return None # return None if there are no authors who have contributed to the magazine with more than 2 articles published
        return authors # return all authors who have contributed to the magazine with more than 2 articles published