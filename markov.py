"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_string = open(file_path).read()

    # print(text_string)
    # print(type(text_string))
    # return "Contents of your file as one long string"
    return text_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

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

    # your code goes here
    # use split() to get list of words
    # loop over list 
    # assign tuple as keys and value as a list with next word
        # use .get() to check if key in chains
            # if key not in chains dictionary, make the value an empty list
            # if key in chains dictionary, append to list

    text_list = text_string.split()

    for i in range(0, len(text_list) -2):

        # makes bigram as tuple key
        tuple_key = (text_list[i], text_list[i +1])

        # next word after bigram
        next_word_value = (text_list[i + 2])


        ### WORKING CODE USING IF-ELSE
        # if tuple_key in chains:
        #     chains[tuple_key].append(next_word_value)
        # else:
        #     chains[tuple_key] = [next_word_value]

        ### TEST CODE USING .GET()
        chains[tuple_key] = chains.get(tuple_key, [])
        chains[tuple_key].append(next_word_value)

    print(chains)


    # return chains
make_chains(open_and_read_file('green-eggs.txt'))
print()
print()
print()
def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
