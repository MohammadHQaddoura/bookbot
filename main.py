# python
from stats import num_words, num_characters, pretty_list
import os
import sys

def get_book_text(path):
    path = os.path.expanduser(path)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	print("============ BOOKBOT ============")
	text = get_book_text(f"{sys.argv[1]}")

	print(f"Analyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")

	text_list = num_words(text)
	print(f"Found {text_list} total words")

	print("--------- Character Count -------\n")

	characters = num_characters(text)
	fin_list = pretty_list(characters)
	for i in fin_list:
		print(f"{i["char"]}: {i["num"]}\n")

	print("============= END ===============")

if __name__ == "__main__":
	main()
