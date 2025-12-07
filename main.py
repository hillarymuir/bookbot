from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    word_count_statement = f"Found {word_count(get_book_text("books/frankenstein.txt"))} total words"
    print(word_count_statement)

main()