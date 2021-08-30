# Name: Pranesh Kathavate
# Batch: Data Science Batch 3
# Topic: Hotel Recommendation System with Machine


import nltk   # Natural LAnguage Toolkit which provide s programmatical interface to users over 100 lexical sources
nltk.download('wordnet')  # Corpus is a collection of written texts and Wordnet can be used to find the meaning of words, synonym or antonym

import numpy as np
import pandas as pd
from nltk.corpus import stopwords       #  A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has 
                                        #  been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query
from nltk.tokenize import word_tokenize    
from nltk.stem.wordnet import WordNetLemmatizer
from ast import literal_eval
nltk.download('punkt')

data = pd.read_csv('HR.csv')

data.head()

# Replacing "United Kingdom with "UK"
data.Hotel_Address = data.Hotel_Address.str.replace("United Kingdom", "UK")
# Now I will split the address and pick the last word in the address to identify the country
data["countries"] = data.Hotel_Address.apply(lambda x: x.split(' ')[-1])
print(data.countries.unique())

data.drop(['Additional_Number_of_Scoring',
       'Review_Date','Reviewer_Nationality',
       'Negative_Review', 'Review_Total_Negative_Word_Counts',
       'Total_Number_of_Reviews', 'Positive_Review',
       'Review_Total_Positive_Word_Counts',
       'Total_Number_of_Reviews_Reviewer_Has_Given', 'Reviewer_Score',
       'days_since_review', 'lat', 'lng'],1,inplace=True)

def impute(column):
    column = column[0]
    if (type(column) != list):
        return "".join(literal_eval(column))
    else:
        return column
    
data["Tags"] = data[["Tags"]].apply(impute, axis=1)
data.head()

data['countries'] = data['countries'].str.lower()
data['Tags'] = data['Tags'].str.lower()


def recommend_hotel(location, description):
    description = description.lower()
    word_tokenize(description)
    stop_words = stopwords.words('english')
    lemm = WordNetLemmatizer()
    filtered  = {word for word in description if not word in stop_words}
    filtered_set = set()
    for fs in filtered:
        filtered_set.add(lemm.lemmatize(fs))

    country = data[data['countries']==location.lower()]
    country = country.set_index(np.arange(country.shape[0]))
    list1 = []; list2 = []; cos = [];
    for i in range(country.shape[0]):
        temp_token = word_tokenize(country["Tags"][i])
        temp_set = [word for word in temp_token if not word in stop_words]
        temp2_set = set()
        for s in temp_set:
            temp2_set.add(lemm.lemmatize(s))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    country['similarity']=cos
    country = country.sort_values(by='similarity', ascending=False)
    country.drop_duplicates(subset='Hotel_Name', keep='first', inplace=True)
    country.sort_values('Average_Score', ascending=False, inplace=True)
    country.reset_index(inplace=True)
    return country[["Hotel_Name", "Average_Score", "Hotel_Address"]].head()



recommend_hotel('Netherlands', 'I loved everything')

recommend_hotel('Netherlands', 'Nice Experience')