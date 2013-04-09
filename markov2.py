from sys import argv
script, txt = argv

import random

def get_text(txt):
	open_file = open(txt)
	captured_text = open_file.read() #parses text, captures string in variable 
	return captured_text

text = get_text(txt)

def strip_punction(text): #commands work in terminal but not in this function
	punc = (",./;'?&-*#][)(0123456789") #identifies unwanted characters using variable
	clean_text = text.translate(None, punc) #removes unwanted characters and numbers
	make_list = clean_text.lower().split() #lowercase all words, split by comma, put into a list
	return make_list

word_list = strip_punction(text)

def make_dictionary(list):
	dictionary = {} #empty dictionary

	for index in range(len(word_list)-2): #subtract 2 words at end of list to prevent breaking
		first = word_list[index] #first word in a list
		second = word_list[index + 1] #second word next to it
		third = word_list[index + 2] #third word next to second
		key = first, second #tuple of two (x, y)

		if key in dictionary: #if the key already exists in d, add the third word to its list of values
			dictionary[key].append(third)
		else:
			dictionary[key] = [third] #if the key does not exist, create it with third as the value
	return dictionary

d = make_dictionary(list)

def make_sentence(d):
	#start with the first three words
	temp_list = [] #empty list to hold incoming words
	word_pair = random.choice(d.keys()) #picks a random set of dictionary keys (x,y)
	temp_list.append(word_pair[0]) #adds first word from key to list
	temp_list.append(word_pair[1]) #adds second word from key to list
	values1 = d.get(word_pair) #finds values associated with the key
	random_value1 = random.choice(values1) #selects 1 random value
	temp_list.append(random_value1)
	#print temp_list
	#### ends first three words

	#### now we make a word chain	

	max_length = 20
	
	for index in range(max_length-2):
		last_words = (temp_list[-2], temp_list[-1])
		if last_words in d:
			values2 = d[last_words]
			next_pair = random.choice(values2)
		else:
			next_pair = random.choice(d.keys())
		temp_list.append(next_pair)
		first = next_pair

	string = " ".join(temp_list)
	sentence = string.capitalize() + "."


	return sentence
print make_sentence(d)











