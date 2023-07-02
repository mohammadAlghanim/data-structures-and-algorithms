
def first_repeated_word(words):
    """
    A function that takes string as argument and returns the first repeated word 
    or returns "No Repetition" if there is no repeated word...
    """
    rep = set()
    for word in words.split():
        if word in rep:
            return word
        else:
            rep.add(word)
    return 'No Repetition'


if __name__ == '__main__':
    print('\n# #################### first_repeated_word function #################### #\n')
    x="Once upon a time, there was a brave princess who..."
    print('> ',x)
    print('\n\tthe first repeated word => ',first_repeated_word(x))
    print('\n***********************************************************')
    y="it was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print('> ',y)
    print('\n\tthe first repeated word => ',first_repeated_word(y))
   