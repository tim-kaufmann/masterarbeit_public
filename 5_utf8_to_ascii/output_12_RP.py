def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        ascii_code = ord(char)
        if ascii_code < 128:  # ASCII characters are in the range 0-127
            ascii_codes.append(ascii_code)
        else:
            ascii_codes.append(ord('?'))  # Replace non-ASCII characters with '?'
    return ascii_codes