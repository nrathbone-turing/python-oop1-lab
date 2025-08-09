#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    # page_count property
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        
        self._page_count = value

    def turn_page(value):
        print("Flipping the page...wow, you read fast!")