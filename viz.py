'''
@Author Benjamin Rittenhouse
@File main.py
@Desc program to identify the structure of a sentence
'''

import spacy

nlp = spacy.load("en_core_web_lg")

# MAIN
inp = ''

while inp != "exit":
	inp = input("Enter a sentence:\n")
	#words = inp.split(' ')
	
	doc=nlp(inp)

	subj = [tok for tok in doc if (tok.dep_ == "nsubj") ]
	obj = [tok for tok in doc if (tok.dep_ == "dobj") ]
	verb = [tok for tok in doc if (tok.dep_ == "ROOT") ]
	

	'''
	print("Subject: ")
	print(subj)
	print("Object: ")
	print(obj)
	print("Verb: ")
	print(verb)
	'''










