import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


filepath = sys.argv[1]

def get_book_text(filepath):

        with open(filepath) as f:
                text = f.read()

        return text

def main():
	
	text = get_book_text(filepath)

	from stats import get_num_words

	num_words = get_num_words(text)

	
	from stats import count_character
	
	counted_characters = count_character(text)

	from stats import sort_data
	
	sorted_char_counts = sort_data(counted_characters)

	
	print("============ BOOKBOT ============")
	print("Analyzing book found at " + str(filepath))
	print("----------- Word Count ----------")
	print("Found " + str(num_words) + " total words")
	print("--------- Character Count -------")
	
	for char, count in sorted_char_counts:
    		if char.isalpha():
        		print(f"{char}: {count}")
	print("============= END ===============")
main()
