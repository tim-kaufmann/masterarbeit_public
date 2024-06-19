def is_valid_variable_name(variable_name: str) -> bool:
    if len(variable_name) > 255:
        return False
    
    if not variable_name[0].isalpha() and variable_name[0] not in ['_', '$']:
        return False
    
    for char in variable_name:
        if not char.isalnum() and char not in ['_', '$']:
            return False
    
    return True
