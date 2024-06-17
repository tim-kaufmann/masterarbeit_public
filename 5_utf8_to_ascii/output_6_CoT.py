def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        # Convert each character to its ASCII code if it is within the ASCII range
        if ord(char) < 128:
            ascii_codes.append(ord(char))
        else:
            # Handle characters outside ASCII range by replacing with a placeholder (e.g., '?')
            ascii_codes.append(ord('?'))
    return ascii_codes