# contains functions for analyzing text

#give word count of whole text
def word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

# count how many times each character appears in the text
def char_count(book_text):
    lc_book_text = book_text.lower()
    char_dict = {}

    for i in range(0, len(lc_book_text)):
        if lc_book_text[i] not in char_dict:
            char_dict[lc_book_text[i]] = 0
        char_dict[lc_book_text[i]] += 1
        
    return char_dict

# sort character count dictionary and generate a formatted report
def generate_report_list(char_count_dict):
    report_list = []

    for key in char_count_dict:
        report_list.append({"char": key, "num": char_count_dict[key]})

    return report_list
