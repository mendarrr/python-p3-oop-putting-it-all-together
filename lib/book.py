#!/usr/bin/env python3
class Book:
    def __init__(self, title, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
            self.page_count = 0
        else:
            self.page_count = page_count
        self.title = title

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")   
    pass
    
        