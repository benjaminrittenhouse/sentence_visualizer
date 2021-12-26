# Demonstration
Please see the demo .mov file to watch the website in action.

# sentence_visualizer

The goal of this project was to create a webapp that lets a user enter sentences that are then parsed and highlighted to show them the different parts of the sentence. This includes the verb, subject, object, etc. 

# design

The flask framework was used along with Python HTML and CSS. The python parses the sentence using the spaCy module to find verbs, nouns, and adjectives. Once these items are found, we note where they occur in the sentence.

Using flask we pass these values back to the HTML side to a div with the respective CSS. Ex. the verb is higlighted red. 

# purpose

This could be used in an educational manner to help students learn how a sentence is structured or even help them when they are stuck trying to figure out what the subject of a sentence is, for example.
