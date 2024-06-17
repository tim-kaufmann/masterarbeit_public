def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        ascii_code = ord(char)
        if ascii_code < 128:  # ASCII range is 0-127
            ascii_codes.append(ascii_code)
        else:
            ascii_codes.append(ord('?'))  # Non-ASCII characters are replaced with '?'
    return ascii_codes
