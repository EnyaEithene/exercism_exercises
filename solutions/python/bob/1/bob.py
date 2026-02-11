def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
            return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()
    
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
