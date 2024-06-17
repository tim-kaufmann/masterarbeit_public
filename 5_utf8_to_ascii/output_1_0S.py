def utf8_to_ascii(utf8_string):
    ascii_codes = []
    for char in utf8_string:
        ascii_code = ord(char)
        if ascii_code < 128:  # Only consider characters in the ASCII range
            ascii_codes.append(ascii_code)
        else:
            # Handle multi-byte UTF-8 characters by replacing them with a placeholder (e.g., '?')
            ascii_codes.append(ord('?'))
    return ascii_codes