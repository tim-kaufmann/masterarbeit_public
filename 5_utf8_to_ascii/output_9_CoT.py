def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        # Convert each character to its ASCII code if it is within the ASCII range
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            # Handle multi-byte characters by ignoring them or replacing them with a placeholder
            ascii_codes.append(ord('?'))  # Using '?' for non-ASCII characters
    return ascii_codes