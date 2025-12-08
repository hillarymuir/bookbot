from stats import word_count, char_count, generate_report_list

# read book text from file into a str
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_location = "books/frankenstein.txt"
    book_text = get_book_text(book_location)
    char_count_dict = char_count(book_text)
    report_list = generate_report_list(char_count_dict)

    #print pretty report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for dict in report_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()