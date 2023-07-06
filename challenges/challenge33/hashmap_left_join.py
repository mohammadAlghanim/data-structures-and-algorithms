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

if __name__ == "__main__":
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
