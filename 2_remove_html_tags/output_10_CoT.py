import re

def remove_html_tags(s):
    # Check if input is a string
    if not isinstance(s, str):
        throw(ValueError("Input must be a string"))
    
    # Return empty string if input is empty
    if s == "":
        return ""
    
    # Define regex patterns
    tag_pattern = re.compile(r'<[^>]+>')
    comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
    doctype_pattern = re.compile(r'<!DOCTYPE[^>]+>', re.IGNORECASE)
    
    # Remove HTML comments
    s = re.sub(comment_pattern, '', s)
    
    # Remove document type declarations
    s = re.sub(doctype_pattern, '', s)
    
    # Remove HTML tags
    s = re.sub(tag_pattern, '', s)
    
    # Trim whitespace from both ends of the string
    return s.strip()
