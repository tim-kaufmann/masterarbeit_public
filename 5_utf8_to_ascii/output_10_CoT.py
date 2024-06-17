def utf8_to_ascii(utf8_string):
    ascii_codes = []
    for char in utf8_string:
        ascii_code = ord(char)
        if ascii_code < 128:
            ascii_codes.append(ascii_code)
        else:
            # Handle multi-byte UTF-8 characters by appending a placeholder value, e.g., -1
            ascii_codes.append(-1)
    return ascii_codes

# Example usage:
# print(utf8_to_ascii("Hello, World!"))
