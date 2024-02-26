#Generating the selected sentences in the utts.data format

my_corpus = "My path"
with open(my_corpus) as file:
    corpus_lines = [line for line in file]

x = 1
y = "000"

for line in corpus_lines:
    line = line.replace("\n", "")

    if x<10:
        print(f'( chloe_horror_{y}{x} "{line}" )')
        x += 1
        
    elif 9<x<100:
        y = "00"
        print(f'( chloe_horror_{y}{x} "{line}" )')
        x += 1
        
    else:
        y="0"
        print(f'( chloe_horror_{y}{x} "{line}" )')
        x += 1

