"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()


    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    words.append(None)

    for i in range(len(words) - 2):
        pair = (words[i], words[i + 1])

        if pair not in chains:
            chains[pair] = [words[i + 2]]
        else:
            chains[pair].append(words[i + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key_list = list(chains.keys())

    first_key = choice(key_list)
    print(f"1: {first_key}")

    while first_key[0][0].upper() != first_key[0][0]:
        first_key = choice(key_list)
        print(f"2: {first_key}")

        if first_key[0][0].upper() == first_key[0][0]:
            words.append(first_key[0])
            words.append(first_key[1])
            # break

            # print(f"First key: {first_key}")
            
            value = choice(chains[first_key])
            words.append(value)
            # print(f"Value: {value}")

    new_key = (first_key[1], value)
    # print(f"New key: {new_key}")
    #for i in range(len(key_list) + 1):
 
    
    while value is not None:
        if new_key in chains:    
            value = choice(chains[new_key])
            words.append(value)
            #print(f"New Value: {new_value}")
        
            if value != None and value[-1] in [".", "?", "!"]: 
                # words.append(value)
                break
            else:
                new_key = (new_key[1], value)
    
   
    words.pop()
    return ' '.join(words)


#input_path = sys.argv[1]
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)