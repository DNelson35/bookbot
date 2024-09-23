def main():
  book = "books/frankenstein.txt"
  txt = get_book_text(book)
  total_words = count_words(txt)
  char_lookup = count_char(txt)
  print_report(total_words, char_lookup)


def get_book_text(book):
  with open(book, "r") as f:
    return f.read()
  
def count_words(txt):
  word_list = txt.split()
  return len(word_list)

def count_char(txt):
  char_dict = {}
  uniform_txt = txt.lower()
  for char in uniform_txt:
    if char in char_dict:
      char_dict[char] += 1
    elif char.isalpha():
      char_dict[char] = 1
    # lambda function for sorting by value instead of key
  return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))




def print_report(word_count, char_lookup):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in document\n")
  for char, value in char_lookup.items():
    print(f"'{char}' character was found {value} times ")
  print("--- End report ---")


main()
