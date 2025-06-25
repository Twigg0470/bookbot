from stats import count_words, character_repeat_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    

def main():
    count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{count} words found in the document")
    print(character_repeat_count(get_book_text("books/frankenstein.txt")))


main()
