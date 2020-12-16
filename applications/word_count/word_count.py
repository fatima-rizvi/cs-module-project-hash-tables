def word_count(s):
    counters = {}    # Create a dictionary to count the number of times each word is in the string
    word_list = s.lower().split()   # Make the string lowercase and split the string into separate words
    for word in word_list:  # Iterate through all of the words in the list
        word = word.strip('":;,.-+=/\\|[]}{()*^&')  # Strip the word of special characters
        if word not in counters: # If the word isn't in our dictionary
            counters[word] = 0 # Add it to counters and set its value to zero ("word" is the key and 0 is the value in this key, value pair in the dictionary)
        # Since the word is now in the dicitonary (or already was)
        counters[word] += 1 # Increment the key's value up by one
   
    return counters # Return the dictionary we made



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))