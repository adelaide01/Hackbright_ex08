"""
Exercise 08 - Markov chains - Thanks to @cjerdonek for your help!

"""

import random
import sys



def get_text(path):
	"""
	Read the file at the given path and return its contents.

	"""
	open_file = open(path)
	captured_text = open_file.read() # parse text, capture string in variable 
	return captured_text


def strip_punction(text): 
	"""
	Remove punctuation and numbers and make a list of words separated by commas.

	"""
	punc = (',./;!"?&-*#][)(0123456789') # identify unwanted characters using variable
	clean_text = text.translate(None, punc) # remove unwanted characters and numbers
	make_list = clean_text.lower().split() # lowercase all words, split by comma, put into a list
	return make_list


def make_dictionary(word_list):
	"""
	Add unique keys to a dictionary along with a corresponding list of values for each key.

	"""

	dictionary = {} # empty dictionary

	for index in range(len(word_list)-2): # subtract two words at end of list to prevent breaking
		first = word_list[index] # first word in a list
		second = word_list[index + 1] # second word next to it
		third = word_list[index + 2] # third word next to second
		key = first, second # tuple of two (x, y)

		if key in dictionary: #if the key already exists in d, add the third word to its list of values
			dictionary[key].append(third)
		else:
			dictionary[key] = [third] # if the key does not exist, create it with third as the value
	return dictionary


def make_sentence(d):
	"""
	Chain words together by starting with a random key pair, then select one its values randomly.

	"""
	# start with the first three words
	temp_list = [] # empty list to hold incoming words
	word_pair = random.choice(d.keys()) # picks a random set of dictionary keys (x,y)
	temp_list.append(word_pair[0]) # adds first word from key to list
	temp_list.append(word_pair[1])  # adds second word from key to list
	values1 = d.get(word_pair)  # finds values associated with the key
	random_value1 = random.choice(values1) # selects 1 random value
	temp_list.append(random_value1)

	#### ends first three words

	#### now we make a word chain	

	max_length = 20
	
	for index in range(max_length-2): # subtract 2 words at end of list to prevent breaking
		last_words = (temp_list[-2], temp_list[-1])
		if last_words in d: # if tuple matches dictionary key
			values2 = d[last_words] # gets the value list of that key
			next_word = random.choice(values2) # selects one value from the list
		else:
			word_pair = random.choice(d.keys()) # in case the key has no values attached, choose random key
			next_word = random.choice(word_pair) # insert the selected words into an empty list

		temp_list.append(next_word) # add to the list
		first = next_word # chain

    # TO DO: remove this try-except that we used for debugging.
	# try:
	# 	string = " ".join(temp_list)
	# except:
	# 	print temp_list
	# 	raise
	
	string = " ".join(temp_list)
	sentence = string.capitalize() + "."

	return sentence


def main():
	script, path = sys.argv
	text = get_text(path)
	word_list = strip_punction(text)

	d = make_dictionary(word_list)
	print d
	print make_sentence(d)

if __name__ == "__main__":
    main()
