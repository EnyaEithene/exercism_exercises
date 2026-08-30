def find_anagrams(word, candidates):
    """Find anagrams of the word given between the candidates
    INPUT:
        word (string): The word for which we need to check for anagrams
        candidates (list of strings): The words in which we need to search for anagrams

    OUTPUT:
        list of strings: The candidates that are indeed anagrams of the given word
    """
    
    anagrams = []                              # Where we store the actual anagrams found
    lower_word = word.lower()                  # 'Normalization' of the word

    for candidate in candidates:
        lower_candidate = candidate.lower()    # 'Normalization' of the candidate

        if lower_candidate == lower_word:      # Avoid candidates that are the exact same as the word
            continue
        
        for letter in lower_word:              # Check existance of letters from word in candidate
            if letter in lower_candidate:
                lower_candidate = lower_candidate.replace(letter, "", 1)
                continue
            break
                
        if not lower_candidate:                # If empty => Has no extra letters that aren't found in word
            anagrams.append(candidate)

    return anagrams
