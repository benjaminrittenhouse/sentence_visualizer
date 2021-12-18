'''
@Author Benjamin Rittenhouse
@File main.py
@Desc program to identify the structure of a sentence
'''



# FUNCTIONS ---- 

# read in verbs from text file
def read_verbs():
	# opening the text file
	verbs = []
	with open('verbs.txt','r') as file:
		for line in file:
			for word in line.split():
				verbs.append(word)

	return verbs


inp = ''

# MAIN

verbs = []
verbs = read_verbs()

while inp != "exit":
	inp = raw_input("Enter a sentence:\n")
	words = inp.split(' ')
	for word in words:
		if word in verbs:
			print("Verb = " + word)
