def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        if ord(char) < 128:  # Only convert characters that are within the ASCII range
            ascii_codes.append(ord(char))
        else:
            # If character is outside ASCII range, append a placeholder value, e.g., '?'
            ascii_codes.append(ord('?'))
    return ascii_codes