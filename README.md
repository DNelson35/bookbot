# Bookbot

This Python script analyzes the contents of a book (in `.txt` format) and generates a report detailing the total number of words and the frequency of each alphabetic character (case-insensitive) found in the text.

## 📄 Description

The default file analyzed is **Mary Shelley's *Frankenstein***, located at `books/frankenstein.txt`. The script performs the following tasks:

1. **Reads the book's text**
2. **Counts the total number of words**
3. **Counts the frequency of each alphabetical character (a-z)**
4. **Prints a simple report to the console**

## 🧠 How It Works

* **`main()`**: Coordinates the execution of the program.
* **`get_book_text(book)`**: Reads the contents of the specified text file.
* **`count_words(txt)`**: Splits the text into words and counts them.
* **`count_char(txt)`**: Counts each letter's frequency, ignoring case and excluding non-alphabetic characters. The results are sorted by frequency in descending order.
* **`print_report(word_count, char_lookup)`**: Displays the analysis results in a readable format.

## 📂 File Structure

```
.
├── books/
│   └── frankenstein.txt
├── main.py       
└── README.md
```

## ✅ Requirements

* Python 3.13.0

## ▶️ Usage

1. Ensure the `frankenstein.txt` file is in a folder named `books/` relative to the script.
2. Run the script:

```bash
python main.py
```

## 📝 Sample Output

```
--- Begin report of books/frankenstein.txt ---
74898 words found in document

'e' character was found 92847 times 
't' character was found 67891 times 
...
--- End report ---
```

## 📌 Notes

* Only alphabetical characters are counted (a-z), and they are normalized to lowercase.
* You can modify the `book` variable in `main()` to analyze any other `.txt` file.

