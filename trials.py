"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    return evens


def get_odd_indices(items):
    result = []

    for i in range(0, len(items)):
        #if index is odd
        if i % 2 == 1:
            result.append(items[i])
    
    return result

def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1

# Return an array of numbers in a certain range.
def get_range(start, stop):
    num_list = []

    for n in range(start, stop):
        num_list.append(n)

    return num_list

def censor_vowels(word):

    #initialize empty list
    chars = []

    #iterate over each letter in given word
    for letter in word:
        #if current letter is a vowel
        if letter in ['a', 'e', 'i', 'o', 'u']:
            #reassign letter to star
            letter = '*'
        #append letter to list
        chars.append(letter)
    
    
    return ''.join(chars)


def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper() + word[1:])
    
    return ''.join(camel_case)
    

def longest_word_length(words):
    long_word =-1
    for word in words:
        if long_word < len(word):
            long_word = len(word)
    
    #print(long_word)
    return long_word
    
longest_word_length(['hello', 'world', 'kamleshpal'])

def truncate(string):
    #create result list 
    result = []

    #iterate over characters in string
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    
    return "".join(result)

print(truncate('aaaaabbbbbcccccddd'))
print(truncate('ccccoooommmppppuuteer'))


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
