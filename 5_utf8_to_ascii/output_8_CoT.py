def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            ascii_codes.append(63)  # ASCII code for '?' as a placeholder for non-ASCII characters
    return ascii_codes