def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        # Convert each character to its ASCII code if possible
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            # For non-ASCII characters, you might want to handle them differently
            # Here we'll just skip them
            continue
    return ascii_codes