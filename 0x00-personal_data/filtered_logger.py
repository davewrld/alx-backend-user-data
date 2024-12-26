#!/usr/bin/env python3

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): The string to replace field values with.
        message (str): The log message.
        separator (str): The field separator in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = '|'.join(f"{field}=.*?(?={separator}|$)" for field in fields)
    return re.sub(
        pattern,
        lambda m: f"{m.group().split('=')[0]}={redaction}",
        message
    )
