import re

def is_valid_variable_name(name: str) -> bool:
    if len(name) > 255:
        return False
    if not re.match(r'^[A-Za-z_$][A-Za-z0-9_$]*$', name):
        return False
    return True