def main():
  book = "books/frankenstein.txt"
  txt = get_book_text(book)
  total_words = count_words(txt)
  print(total_words)


def get_book_text(book):
  with open(book, "r") as f:
    return f.read()
  
def count_words(txt):
  word_list = txt.split()
  return len(word_list)


main()
