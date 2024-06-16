import re

def remove_html_tags(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not s:
        return ""
    
    # Define regex patterns
    tag_pattern = re.compile(r'<[^>]+>')
    comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
    doctype_pattern = re.compile(r'<!DOCTYPE[^>]*>', re.IGNORECASE)
    
    # Remove HTML comments
    s = re.sub(comment_pattern, '', s)
    # Remove document type declarations
    s = re.sub(doctype_pattern, '', s)
    # Remove HTML tags
    s = re.sub(tag_pattern, '', s)
    
    return s.strip()
