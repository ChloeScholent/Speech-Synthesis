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


#Sorting the dictionary by frequency value from the highest to the lowest
sorted_dic_diphones = sorted(dic_diphones.items(), key=lambda x:x[1], reverse=True)
converted_dic_diphones = dict(sorted_dic_diphones)


#List of diphones needed (less than 6 in terms of frequency)
needed_diphones = []
for key, value in converted_dic_diphones.items():
    if value < 6 :
        needed_diphones.append(key)




#My corpus: diphones (key) aligned with sentences (value).
my_corpus = "Corpus.txt"
with open(my_corpus) as file:
    corpus = file.read()
corpus = re.sub("[\n]","",corpus)

corpus_sentences = sent_tokenize(corpus)
corpus_phones = [g2p(sentence) for sentence in corpus_sentences]
corpus_diphones = [generate_diphones_with_sil(g2p(sentence)) for sentence in corpus_sentences]


#Loop to have the indexes of the sentences in which needed_diphones are present
test = []
for i in corpus_diphones:
    for j in i:
        for k in needed_diphones:
            if j == k:
                test.append(corpus_diphones.index(i))


#The frequency of needed diphones per sentence indexed 
needed_diphones_frequency_dict = {}
for key in test:
     if key in needed_diphones_frequency_dict:
        needed_diphones_frequency_dict[key] += 1
     else:
          needed_diphones_frequency_dict[key] = 1


#Sort the dictionary in order to have the index of the sentences with the most needed diphones first
sorted_needed_diphones_frequency_dict = sorted(needed_diphones_frequency_dict.items(), key=lambda x:x[1], reverse=True)
converted_needed_diphones_frequency_dict = dict(sorted_needed_diphones_frequency_dict)        


#Create a list with the indexes of the needed sentences
needed_sentences = []
for key, value in converted_needed_diphones_frequency_dict.items():
    if value > 3 :
        needed_sentences.append(key)


#Print the actual sentences to be added to the script, sorted by their length
def sorting(lst):
    lst.sort(key=len)
    return lst

needed_sentences_list = []
for i in needed_sentences:
    needed_sentences_list.append(corpus_sentences[i])

sorted_sentences = sorting(needed_sentences_list)
for i in sorted_sentences:
    print(i)




