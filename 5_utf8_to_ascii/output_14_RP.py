def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        # Convert character to ASCII if it's within ASCII range
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            # Handle non-ASCII characters (multi-byte UTF-8 characters)
            ascii_codes.append(ord('?'))  # Using '?' for non-ASCII characters
    return ascii_codes