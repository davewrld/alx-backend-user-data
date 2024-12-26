#!/usr/bin/env python3

"""function that returns log messege obfusscated"""

import logging
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Intialize formatter with fields to filter

        Args:
            fields (List[str]): to be obfuscated

        """

        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log recorfd to filter sensitive fields"""

        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super().format(record)
