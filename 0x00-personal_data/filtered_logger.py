#!/usr/bin/env python3

import re

"""Function that returns the message obfuscated"""

def filter_datum(fields: str, redaction: str, message: str, separator: str) -> str:
    pattern = '|'.join(f"{field}=.*?(?={separator}|$)" for field in fields)
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)
