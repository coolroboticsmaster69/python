def print_length(user_input):
	words = user_input.split()
	print ("this is the length of the sentence: " + str(len(words)))


def rev_string(user_input):
	rev_str = ""
	for x in xrange(len(user_input)-1,-1,-1):
		rev_str = rev_str + user_input[x]
	print ("this is the reverse of your sentence: " + rev_str)	

def rev_words(user_input):
	# Now reverseing the sentence by words
	words = user_input.split()	
	words.reverse()
	rev_words_str = ""
	for word in words:
		rev_words_str = rev_words_str + word + " "
	print ("this is the reverse of words in your sentence: " + rev_words_str)



sentence=raw_input("enter a sentence: ")
print_length(sentence)
rev_string(sentence)
rev_words(sentence)