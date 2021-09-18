# Shagov Aleksei
import re

def word_stats(texts):
    count_entry = {}
    convert_list = []
    num_line = {}

    for line, text in enumerate(texts):
        convert_text = re.sub('([^A-z^\s])+', '', text).lower()
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
