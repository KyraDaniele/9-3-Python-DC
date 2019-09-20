word = input("Give me a word: ")

all_freq = {} 

for i in word: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
print(all_freq)