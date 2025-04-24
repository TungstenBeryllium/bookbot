def get_num_words(text):
	
	words = text.split()
	num_words = len(words)
	
	return num_words


def count_character(text):
	counted_chars = {}
	lowered = text.lower()
	
	for char in lowered:
		if char not in counted_chars:
			counted_chars[char] = 1
		else:
			counted_chars[char] += 1
	return counted_chars


def sort_data(counted_chars):  # Accept the dictionary from `count_character`

	sorted_data = sorted(counted_chars.items(), key=lambda x: x[1], reverse=True)
	return sorted_data
