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
			sj = str(pieces[0])
			sj = sj[1:len(sj)-1]

			oj = str(pieces[1])
			oj = oj[1:len(oj)-1]

			v = str(pieces[2])
			v = v[1:len(v)-1]

			rendered = ""

			allwords = sentence.split(' ')
			for word in allwords:
				if word == sj:
					rendered += "<span class = 'highlight'>" + sj + "</span>"
				elif word == oj:
					rendered += "<span class = 'highlight'>" + oj + "</span>"
				elif word == v:
					rendered += "<span class = 'highlight'>" + v + "</span>"
				else:
					rendered += word + " "


			ret =  "<input name = \"user_sentence\" id = \"sentence\" type=\"sentence\" value=\"" + {{rendered}} + "\" />"


			return render_template('index_updated.html', completed_input = ret)
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










