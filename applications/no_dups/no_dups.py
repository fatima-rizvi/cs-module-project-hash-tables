def no_dups(s):
    split_sent = s.split()  # split the string
    output = ''                # create a variable to hold the output
    for word in split_sent:     # For each word in the split string
        if output.find(word) == -1: # Look in the output to see if the word is not in it. -1 means false, its not in there
            output += word + ' '    # If it isn't add the word to the output after a space
    return output.strip(' ')                # Return the output with .strip to get rid of any trailing whitespace


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))