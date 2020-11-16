from probe_hash_map import ProbeHashMap

table = ProbeHashMap()
file = open("count_words.txt", "r")
# To do

max_word = ""
max_count = 0

for i in file.read().lower().split():
    if i not in table:
        table[i] = 1
    else:
        table[i] += 1

for word in table:
    if table[word] > max_count:
        max_count = table[word]
        max_word = word

print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)
#print('The freq of the word "Mark" is ', table['mark'])
