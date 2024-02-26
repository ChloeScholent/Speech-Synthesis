my_corpus = "My path"
with open(my_corpus) as file:
    corpus_lines = [line for line in file]

x = 1
y = "000"

for i in corpus_lines:
    i = i.replace("\n", "")

    if x<10:
        print(f'( chloe_horror_{y}{x} "{i}" )')
        x += 1
        
    elif 9<x<100:
        y = "00"
        print(f'( chloe_horror_{y}{x} "{i}" )')
        x += 1
    elif x>99:
        y="0"
        print(f'( chloe_horror_{y}{x} "{i}" )')
        x += 1

