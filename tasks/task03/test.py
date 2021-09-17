
import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

converted_list = []
count = {}
lines = {}

for line_number, text in enumerate(texts):
    converted_text = re.sub('([^A-z^\s])+', '', text).lower() 
    converted_words = converted_text.split()

    for converted_word in converted_words:
        converted_list.append(converted_word)
        count[converted_word] = converted_list.count(converted_word)
        
        if converted_word not in lines:
            lines[converted_word] = line_number

print(f"word\tcount\tfirst line")
for key in count:
    print(f"{key}\t{count[key]}\t{lines[key]}")