import re

def remove_html_tags(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    if s == "":
        return ""

    tag_pattern = re.compile(r'<[^>]+>')
    comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
    doctype_pattern = re.compile(r'<!DOCTYPE[^>]*>', re.IGNORECASE)

    s = re.sub(comment_pattern, '', s)
    s = re.sub(doctype_pattern, '', s)
    s = re.sub(tag_pattern, '', s)

    return s.strip()
