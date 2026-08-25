def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_list = list(alphabet)
    code = ""
    
    for i in text:
        if i.lower() in alpha_list:
            index = alpha_list.index(i.lower())
            if i == i.upper():
                code += alpha_list[(index + key) % 26].upper()
            else:
                code += alpha_list[(index + key) % 26]
        else:
            code += i  # keep spaces/punctuation
    
    return code

