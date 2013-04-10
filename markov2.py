Thanks to @cjerdonek for your help on this exercise!

from sys import argv
script, txt = argv

from random import choice

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
	#ends first three words

	#now make a word chain using the first three words	

	max_length = 20
	
	for index in range(max_length-2):
		last_words = (temp_list[-2], temp_list[-1]) #pulls the last two words from the list, and formats it as a tuple
		if last_words in d: #if tuple matches dictionary key
			values2 = d[last_words] #gets the value list of that key
			next_pair = random.choice(values2) #selects one value from the list 
		else:
			next_pair = random.choice(d.keys()) #in case the key has no values attached, choose random key
		temp_list.append(next_pair) #insert the selected words into an empty list
		first = next_pair #chain

	string = " ".join(temp_list) #creates string from list
	sentence = string.capitalize() + "." #capitalizes the first letter of the sentence and ends with a period.


	return sentence
print make_sentence(d)











