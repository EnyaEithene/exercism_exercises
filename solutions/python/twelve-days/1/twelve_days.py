def recite(start_verse, end_verse):
    """Recites the selected verses of the song "The Twelve Days of Christmas"
    INPUT:
        start_verse (integer): The first verse to start from
        end_verse (integer): The last verse to finish with

    OUTPUT:
        list of strings: A list that contains each verse that was asked for
    """

    # The final result
    output_lyrics = []

    # The lyric components
    common_lyrics = ("On the ",
             " day of Christmas my true love gave to me: ")

    day = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")

    gifts = ("a Partridge in a Pear Tree.",
             "two Turtle Doves, ",
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, ")

    # Putting them together based on what verses are asked in the input
    for verse_number in range(start_verse-1, end_verse):
        verse = ""
        
        # First phrase
        verse += common_lyrics[0] + day[verse_number] + common_lyrics[1]

        # Gifts
        for item in gifts[verse_number::-1]:
            if item == gifts[0] and verse_number > 0:
                verse += "and " + item
            else:
                verse += item

        # Add to final list
        output_lyrics.append(verse)

    return output_lyrics
