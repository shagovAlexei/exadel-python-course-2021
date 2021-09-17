# Shagov Aleksei

'''You are given a list of sentences. Find all unique words along with:
Number of word occurrences
Number of the sentence where the word appeared for the first time

Note: ignore word case during comparison, i.e. treat “Home”, “home” and “HOME” as the same words.

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

word    count   first line
hello   2       0
world   2       0
the     1       1
is      1       1
mine    1       1
how     1       2
are     1       2
you     1       2

'''
import re

def word_stats(texts):
    count_entry = {}
    convert_list = []
    num_line = {}

    for line, text in enumerate(texts):
        # print(line, text)
        convert_text = re.sub('([^A-z^\s])+', '', text).lower()
        # print(convert_text)
        convert_words = convert_text.split()
        for convert_word in convert_words:
            convert_list.append(convert_word)
            count_entry[convert_word] = convert_list.count(convert_word)
            if convert_word not in num_line:
                num_line[convert_word] = line

    print("word\tcount\tfirst line")
    for key in count_entry:
        print(f"{key} \t{count_entry[key]} \t{num_line[key]}")

def main():
    texts = [
      "Hello, World!",
      "The world is mine",
      "Hello, how are you?"
    ]
    word_stats(texts)

if __name__ == "__main__":
    main()
