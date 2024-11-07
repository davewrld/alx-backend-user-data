#!/usr/bin/env/python3

import re

"""Function that returns the message obfuscated"""


def filter_datum(fields: list, redaction: str, message: str, separator: str):
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)
