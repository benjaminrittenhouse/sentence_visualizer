'''
@Author Benjamin Rittenhouse
@File main.py
@Desc program to identify the structure of a sentence
'''

import spacy
from flask import *
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		sentence_inp = request.form.get('user_sentence')
		if sentence_inp != '':
			sentence = request.form['user_sentence']
			pieces = [] # pieces of sentence init
			pieces = parse_sentence(sentence)
			return render_template('index_updated.html', subject = pieces[0], object = pieces[1], verb = pieces[2])
	else:
		return render_template('index.html')

nlp = spacy.load("en_core_web_lg")

# MAIN

	#words = inp.split(' ')
def parse_sentence(s):

	doc=nlp(s)

	subj = [tok for tok in doc if (tok.dep_ == "nsubj") ]
	obj = [tok for tok in doc if (tok.dep_ == "dobj") ]
	verb = [tok for tok in doc if (tok.dep_ == "ROOT") ]

	ret = []
	ret.append(subj)
	ret.append(obj)
	ret.append(verb)

	return ret










