from stats import word_count, char_count

# read book text from file into a str
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count_statement = f"Found {word_count(book_text)} total words"
    print(word_count_statement)
    print(char_count(book_text))

main()