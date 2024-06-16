import re

def remove_html_tags(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if s == "":
        return ""

    tag_pattern = re.compile(r'<[^>]+>')
    comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
    doctype_pattern = re.compile(r'<!DOCTYPE[^>]+>', re.IGNORECASE)

    # Remove HTML comments
    no_comments = re.sub(comment_pattern, '', s)
    # Remove document type declarations
    no_doctype = re.sub(doctype_pattern, '', no_comments)
    # Remove HTML tags
    no_tags = re.sub(tag_pattern, '', no_doctype)

    return no_tags.strip()
