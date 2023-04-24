import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass
    
############################################################
# Callback function called on each execution pass
############################################################

def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    import wikipedia

    # Define function to preprocess input text
    def preprocess(text):
        # Tokenize input text
        tokens = nltk.word_tokenize(text)

        # Part-of-speech tag tokens
        pos_tags = nltk.pos_tag(tokens)

        # Lemmatize tokens
        lemmatizer = nltk.WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token, pos=get_wordnet_pos(pos_tag)) for token, pos_tag in pos_tags]

        # Remove stopwords and punctuation
        stopwords = nltk.corpus.stopwords.words('english')
        clean_tokens = [token for token in lemmatized_tokens if token.lower() not in stopwords and token.isalnum()]

        return clean_tokens

    # Define function to map part-of-speech tags to WordNet POS tags
    def get_wordnet_pos(pos_tag):
        if pos_tag.startswith('J'):
            return nltk.corpus.wordnet.ADJ
        elif pos_tag.startswith('V'):
            return nltk.corpus.wordnet.VERB
        elif pos_tag.startswith('N'):
            return nltk.corpus.wordnet.NOUN
        elif pos_tag.startswith('R'):
            return nltk.corpus.wordnet.ADV
        else:
            return nltk.corpus.wordnet.NOUN # default to noun if no other match

    # Define function to retrieve answer from Wikipedia
    def retrieve_answer(question):
        try:
            # Search Wikipedia for the question
            search_results = wikipedia.search(question)

            # Use the first search result to get the page summary
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = page.summary

            # Return the first sentence of the summary as the answer
            answer = nltk.sent_tokenize(summary)[0]

        except:
            # If there is an error, return a generic message
            answer = "I'm sorry, I don't know the answer to that question."

        return answer

    # Define function to generate chatbot response
    def generate_response(text):
        # Preprocess input text
        tokens = preprocess(text)

        # Combine tokens into question
        question = " ".join(tokens)

        # Retrieve answer from Wikipedia
        answer = retrieve_answer(question)

        return answer

    # Process input text and generate response for each message in the request
    output = []
    for text in request.text:
        response = generate_response(text)
        output.append(response)

    # Return output
    return SimpleText(dict(text=output))

