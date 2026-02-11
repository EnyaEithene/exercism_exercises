def is_pangram(sentence):
    sentence = sentence.lower()
    letters = set(c for c in sentence if c.isalpha())
    return len(letters) == 26
