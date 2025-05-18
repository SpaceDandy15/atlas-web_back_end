import re

def filter_datum(fields, redaction, message, separator):
    pattern = r'(' + '|'.join(fields) + r')=([^' + re.escape(separator) + r']*)'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
