def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        if ord(char) < 128:  # ASCII characters are in the range 0-127
            ascii_codes.append(ord(char))
        else:
            ascii_codes.append(ord('?'))  # Non-ASCII characters are replaced with '?'
    return ascii_codes