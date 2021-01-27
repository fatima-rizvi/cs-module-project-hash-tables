# Your code here

def histo(textfile):
    with open(textfile), 'r') as file_output: # open the file as readable
        data = file_output.read()

    #Get words in an array, form an arr from this data
    word_arr = data.split()

    cache = {}

    for word in word_arr:
        word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')
        if word not in cache:
            # add word to cache
            cache[word] = []

        else:
            cache[word].append('#') # add hashtag to thecache at the end as a visible rep of the count

    for word, count in cache.items():
        print(f'{word}    {count}')
        

histo('robin.txt')