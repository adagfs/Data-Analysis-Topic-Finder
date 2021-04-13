import math
import nltk

#Read the file, labelled document
f = open('document.txt')
raw = f.read()

# Splits the input into paragraphs that can now be processed
splitInput = raw.split("\n");





#IMPORTANT NOTE: This code is taken (and mildly tweaked) from https://github.com/yebrahim/TF-IDF-Generator
#You may find the code in question in the tfidf.py file from the link


# a list of (words-freq) pairs for each document
global_terms_in_doc = {}
# list to hold occurrences of terms across documents
global_term_freq    = {}

#get list of common english words
stopwords = nltk.corpus.stopwords.words('english')

#remove list of common words
def remove_stopwords(text):
    # remove punctuation
    chars = ['.', '/', "'", '"', '?', '!', '#', '$', '%', '^', '&',
             '*', '(', ')', ' - ', '_', '+', '=', '@', ':', '\\', ',',
             ';', '~', '`', '<', '>', '|', '[', ']', '{', '}', '–', '“',
             '»', '«', '°', '’']
    for c in chars:
        text = text.replace(c, ' ')

    text = text.split()

    import nltk
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower().strip() not in stopwords]
    return content

#Find frequency of words in paragraphs and in overall document
for paragraph in splitInput:
    terms_in_doc = {}

    paragraph_words = remove_stopwords(paragraph)

    for word in paragraph_words:
       if word in terms_in_doc:
           terms_in_doc[word]+= 1
       else:
           terms_in_doc[word] = 1

       if word in global_term_freq:
           global_term_freq[word] += 1
       else:
           global_term_freq[word] = 1

    global_terms_in_doc[paragraph] = terms_in_doc


#find the tf-idk value for each
topic_para_pair = [];
for paragraph in splitInput:

    result = []
    # calculate tf-idf, put in new list
    max_freq = 0
    for (term,freq) in global_terms_in_doc[paragraph].items():
        if freq > max_freq:
            max_freq = freq
    for (term,freq) in global_terms_in_doc[paragraph].items():
        idf = math.log(float(1 + len(paragraph)) / float(1 + global_term_freq[term]))
        tfidf = float(freq) / float(max_freq) * float(idf)
        result.append([tfidf, term])



    # sort result on tfidf and write them in descending order
    result = sorted(result, reverse=True)
    topic_para_pair.append([paragraph, [result[0][1], result[1][1], result [2][1]]]);




#Write this into a csv file
import pandas as pd
df = pd.DataFrame(topic_para_pair)
df.to_csv('filename.csv', index=False, header=["Paragraphs", "Topics"])