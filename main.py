def get_book_text(path_to_file):
    with open(path_to_file) as booktext:
        book_contents = booktext.read()
    return book_contents

from stats import count_words
from stats import count_characters
from stats import sort_dictionary
import sys

def main():
     #print(len(sys.argv))
     if len(sys.argv) < 2:
          print("Usage: python3 main.py <path_to_book>")
          sys.exit(1)
     book_path = sys.argv[1]

     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {book_path}...")
     
     

     print("----------- Word Count ----------")
     num_words = count_words(
         get_book_text(book_path)
     )
     print(f"Found {num_words} total words")
     
     print("--------- Character Count -------")
     
     sorted_list = sort_dictionary((count_characters(get_book_text(book_path))))
     #print(sorted_list)
     for dict_piece in sorted_list:
        # print(dict_piece)
         c = dict_piece["char"]
         n = dict_piece["num"]
         if c.isalpha():
                 print(f"{c}: {n}")
                 #print(f"{dict_piece["char"]}: {dict_piece["num"]}")

main()
