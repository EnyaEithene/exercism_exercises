def translate(text):
    def translate_word(word):
        vowels = ("a", "e", "i", "o", "u")

        # Rule 1
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        i = 0
        while i < len(word):
            if word[i] in vowels:
                break
            if word[i] == "y" and i != 0:
                break
            if word[i:i+2] == "qu":
                i += 2
                break
            i += 1

        return word[i:] + word[:i] + "ay"

    return " ".join(translate_word(word) for word in text.split())