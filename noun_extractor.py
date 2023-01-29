import nltk

def noun_extractor(text):

    from nltk.corpus import stopwords

    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append("Write")
    stopwords.append("=")
    stopwords.append("*")
    stopwords.append("Select")
    stopwords.append("AND")
    stopwords.append("Insertions")
    stopwords.append("SQL")
    stopwords.append("Query")
    stopwords.append("Creation")
    stopwords.append("Create")
    stopwords.append("Extend")
    stopwords.append("Number")
    stopwords.append("Travels")
    stopwords.append("Delete")
    stopwords.append("Test")
    stopwords.append("Add")
    stopwords.append("Char")
    stopwords.append(">")
    stopwords.append("<")
    stopwords.append("/p")
    stopwords.append("/div")
    stopwords.append("Table")
    stopwords.append("Use")
    stopwords.append("Hint")
    stopwords.append("Domain")
    stopwords.append("Prepare")
    stopwords.append("DBMS")

    from nltk.tokenize import word_tokenize, sent_tokenize


    def ProperNounExtractor(text):
         #print('PROPER NOUNS EXTRACTED :')

        words1 = []
        words = nltk.word_tokenize(text)
        words = [word for word in words if word not in set(stopwords)]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NNP':  # If the word is a proper noun
                words1.append(word)
                    # print(word)
        return(words1)
    a= ProperNounExtractor(text)
    return a


