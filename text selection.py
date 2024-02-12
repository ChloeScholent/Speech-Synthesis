#TO DO
#Faire une liste avec mes phrases
#Itérer sur la liste et créer liste de diphone pour chaque phrase
#itérer sur la nouvelle liste pour trouver les diphones nécessaires
#et créer un rang par la fréquence d'apparition encore, puis trier avec les phrases les plus efficaces

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import re
from g2p_en import G2p


#############################################


arctica_b = "cmuarcticab.data.txt"

with open(arctica_b, 'r') as file:
    source = file.read()

source = re.sub("[0-9]","",source)
source = source.replace("arctic_a", "")
source = source.replace("arctic_b", "")
source = re.sub("[()]","",source)
source = ''.join(i for i in source if i not in '"')


#Tokenize the text into sentences and then into phones
sentences = sent_tokenize(source)
g2p = G2p()
phones = [g2p(sentence) for sentence in sentences]


#Generate diphones and adding SIL at the beginning and end of each diphone list
def generate_diphones_with_sil(phones):
    phones_with_sil = ['SIL'] + phones + ['SIL']
    return [f"{phones_with_sil[i]}-{phones_with_sil[i+1]}" for i in range(len(phones_with_sil)-1)]

diphones_per_sentence = [generate_diphones_with_sil(g2p(sentence)) for sentence in sentences]


#Dictionary of diphone frequency in the "arctic a and b" text    
dic_diphones = {}

for phone_list in diphones_per_sentence:
   for index in phone_list:
       if index in dic_diphones:
               dic_diphones[index] += 1
       else:
               dic_diphones[index] = 1
#print(dic_diphones)


#Sorting the dictionary by frquency value from the highest to the lowest
sorted_dic_diphones = sorted(dic_diphones.items(), key=lambda x:x[1], reverse=True)
converted_dic_diphones = dict(sorted_dic_diphones)


#List of diphones needed (less than 6 in terms of frequency)
needed_diphones = []
for key, value in converted_dic_diphones.items():
    if value < 6 :
        needed_diphones.append(key)

#print(len(converted_dic_diphones))


#My corpus: diphones (key) aligned with sentences (value). (In a dictionary ?)
my_corpus = "SCP script.txt"
with open(my_corpus) as file:
    corpus = file.read()
corpus = re.sub("[\n]","",corpus)


corpus_sentences = sent_tokenize(corpus)
corpus_phones = [g2p(sentence) for sentence in corpus_sentences]
corpus_diphones = [generate_diphones_with_sil(g2p(sentence)) for sentence in corpus_sentences]


corpus_diphones_tuples = []
for x in corpus_diphones:
    corpus_diphones_tuples.append(tuple(x))


result_dict_diphones = dict.fromkeys(corpus_diphones_tuples)
 
for key, value in zip(result_dict_diphones.keys(), corpus_sentences):
    result_dict_diphones[key] = value
 
#print(result_dict_diphones)


#Selection: sorting by highest number of needed diphones in shortest sentence (in two steps ?)

for i in needed_diphones:
    needed_sentences = result_dict_diphones.get(i)

print(needed_sentences)
