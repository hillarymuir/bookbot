# contains functions for analyzing text

def word_count(book_text):
    word_list = book_text.split()
    return len(word_list)