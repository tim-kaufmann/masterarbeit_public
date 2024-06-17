def utf8_to_ascii(input_string):
    ascii_codes = []
    for char in input_string:
        if ord(char) < 128:  # ASCII range is 0-127
            ascii_codes.append(ord(char))
        else:
            # Handling non-ASCII characters by ignoring them
            ascii_codes.append(63)  # ASCII code for '?'
    return ascii_codes

# Example usage:
# result = utf8_to_ascii("Hello, World!")
# print(result)  # [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
