#!/usr/bin/env python3
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    pattern = r'(' + '|'.join(fields) + r')=([^' + re.escape(separator) + r']*)'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
