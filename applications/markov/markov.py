import random

def markov(words):
    cache = {}
    words_arr = words.split()

    for i in range(len(words_arr) - 1):
        word = words_arr[i].lower().strip('":;,.-+=/\\|[]}{()*^&')              # keeps track of word
        next_word = words_arr[i + 1].lower().strip('":;,.-+=/\\|[]}{()*^&')     # keeps track of word that comes next
        
        if word not in cache:                           # if the word is not in cache, add it to a new dictionary
            cache[word] = {}

        if next_word not in cache[word]:
            cache[word][next_word] = 0
        cache[word][next_word] += 1                     # value of next word at word incremented by 1

    for word in cache:                                  # all words should be in dictionary when we enter for loop
        next_words = cache[word]
        total = 0
        
        for word in next_words:
            count = next_words[word]                    # counts all the things in next_words
            total += count
    
        for word in next_words:
            next_words[word] /= total

    return cache


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    chain = markov(words)

    counter = 0                                     # counts how many sentences we have created

    while counter < 5:                              # only want to create 5 random sentences
        counter += 1
        sentence = ["the"]

        while len(sentence) < 8:
            rand_num = random.random()                   # picks a random number and assigns it to a variable, limits how long the sentence can be
            word = sentence[-1]                          # picks very last word in the sentence
            total = 0

            for next_word in chain[word]:
                total += chain[word][next_word]          # accessing word and next word in the markov chain

                if total > rand_num:                     # when we reach the random sentece length we created, we break out of the loop 
                    sentence.append(next_word)
                    break

        print(" ".join(sentence))
            

# todo: analyze which words can follow other words

# todo: construct 5 random sentences