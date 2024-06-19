def is_valid_variable_name(name: str) -> bool:
    if len(name) == 0 or len(name) > 255:
        return False
    
    if not (name[0].isalpha() or name[0] in ['_', '$']):
        return False

    for char in name[1:]:
        if not (char.isalnum() or char in ['_', '$']):
            return False

    return True