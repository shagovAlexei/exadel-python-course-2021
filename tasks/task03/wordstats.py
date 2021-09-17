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

def Word_Stats(texts):
	count_entry = {}
	converted_list = []
	num_line = {}

	for line_number, text in enumerate(texts):
			print(line_number, text)
			converted_text = re.sub('([^A-z^\s])+', '', text).lower()
			converted_words = converted_text.split()
			for converted_word in converted_words:
					converted_list.append(converted_word)
					count_entry[converted_word] = converted_list.count(converted_word)
					if converted_word not in num_line:
						num_line[converted_word] = line_number


	print("word\tcount\tfirst line")
	for key in count_entry:
		print(f"{key} \t{count_entry[key]} \t{num_line[key]}")

def main():
	texts = [
			"Hello, World!",
			"The world is mine",
			"Hello, how are you?"
	]
	
	Word_Stats(texts)

if __name__ == "__main__":
	try:
		main()
	except:
		print("Error!!! Something went wrong.")
