def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def main():
    word_count_statement = f"Found {word_count(get_book_text("books/frankenstein.txt"))} total words"
    print(word_count_statement)

main()