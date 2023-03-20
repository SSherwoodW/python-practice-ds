def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase_lst = phrase.split()
    capital = phrase_lst[0].capitalize()
    phrase_lst.pop(0)
    phrase_lst.insert(0, capital)
    new_phrase = ",".join(phrase_lst)
    return new_phrase
    
