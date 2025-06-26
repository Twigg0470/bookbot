from stats import count_words, character_repeat_count, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")

    text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    count = count_words(text)
    print(f"Found {count} total words")
    
    sorted_list = sort_dict(character_repeat_count(text))
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
   
    print("============= END ===============")

main()
