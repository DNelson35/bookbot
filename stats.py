import sys

def count_words(txt):
  word_list = txt.split()
  return len(word_list)

def get_book_text(book):
  with open(book, "r") as f:
    return f.read()
  


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
  print(f"--- Begin report of {sys.argv[1]} ---")
  print(f"{word_count} words found in the document\n")
  for char, value in char_lookup.items():
    print(f"{char}: {value}")
  print("--- End report ---")

