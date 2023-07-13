def left_join(synonyms, antonyms):
    """
    Performs a LEFT JOIN operation on two hash maps.

    Args:
        synonyms (dict): The first hash map with word strings as keys and synonym values.
        antonyms (dict): The second hash map with word strings as keys and antonym values.

    Returns:
        list: The resulting data structure that holds the LEFT JOINed key-value pairs.
    """
    result = []

    for key, value in synonyms.items():
        if key in antonyms:
            result.append([key, value, antonyms[key]])
        else:
            result.append([key, value, None])

    return result
def most_common_word(book):
    word_counts = {}
    temp_word = ""
    temp_counter = 0
    words = book.lower().split()
    for word in words:
        if word == "":
            continue
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        if word_counts[word] >= temp_counter:
            temp_word = word
            temp_counter = word_counts[word]

    return temp_word

def has_unique_characters(string):
    char_set = set()
    string = string.lower().replace(" ", "")
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)

    return True








if __name__ == "__main__":
    string1 = "The quick brown fox jumps over the lazy dog"
    print(has_unique_characters(string1))  # Output: False

    string2 = "Donald the duck"
    print(has_unique_characters(string2))  # Output: True
    # book = "Taco cat ate a taco"
    # most_common = most_common_word(book)
    # print("The most common word in the book is:", most_common)

    synonyms = {
    "a": 1,
    "b": 3,
    "c": 2,
    "d": 3,
    "e": 5,
}

    antonyms = {
    "b": 3,
    "d": 4,
    "e": 5
}
    result = left_join(synonyms, antonyms)
    print(result)
