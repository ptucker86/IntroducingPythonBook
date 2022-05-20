def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

# giving it some punch
def enliven(word):
    return word.capitalize() + '!'

# edit_story(stairs,enliven)

# performs enliven inline
edit_story(stairs, lambda word: word.capitalize() + '!')