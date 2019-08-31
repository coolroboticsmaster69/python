def print_length(user_input):
	words = user_input.split()
	print ("this is the length of the sentence: " + str(len(words)))


def rev_string(user_input):
	rev_str = ""
	for x in range(len(user_input)-1,-1,-1):
		rev_str = rev_str + user_input[x]
	print ("this is the reverse of your sentence with reversed word: " + rev_str)	

def rev_sentence(user_input):
	# Now reverseing the sentence by words
	words = user_input.split()	
	words.reverse()
	rev_words_str = ""
	for word in words:
		rev_words_str = rev_words_str + word + " "
	print ("this is the reverse of your sentence: " + rev_words_str)



sentence = input("enter a sentence: ")
print_length(sentence)
rev_sentence(sentence)
rev_string(sentence)