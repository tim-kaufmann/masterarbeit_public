def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        # Convert each character to its ASCII code, ignoring non-ASCII characters
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            ascii_codes.append(ord('?'))  # Placeholder for non-ASCII characters
    return ascii_codes
