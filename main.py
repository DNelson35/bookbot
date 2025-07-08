from stats import count_words, count_char, print_report, get_book_text
import sys

def main():
  # "books/frankenstein.txt"
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book = sys.argv[1]
  txt = get_book_text(book)
  total_words = count_words(txt)
  char_lookup = count_char(txt)
  print_report(total_words, char_lookup)

main()
