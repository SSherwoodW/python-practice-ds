def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    f_dict = {}
    vowels = ['a','e','i','o','u']

    for i in phrase:
        if i.lower() in vowels:
            if i in f_dict:
                f_dict[i] += 1
            else:
                f_dict[i] = 1
    
    return f_dict
