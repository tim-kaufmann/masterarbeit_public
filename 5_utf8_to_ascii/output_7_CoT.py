def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            # Handle non-ASCII characters by replacing them with a placeholder or skipping
            ascii_codes.append(ord('?'))  # Using '?' as a placeholder for non-ASCII characters
    return ascii_codes