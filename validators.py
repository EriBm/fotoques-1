"""
Based on http://framework.zend.com/manual/en/zend.validate.set.html
"""

class ValidatorException(Exception):
    
    def __init__(self, value, expected):
        self.value = value
        self.expected = expected
    
    def __str__(self):
        return "Wrong value " + repr(self.value) + ". " + self.expected + " value expected"

def Alnum(value):
    """
    Only alphabetical characters and digits
    """
    if value.isalnum():
        return value
    else:
        raise ValidatorException(value, "Alphanumerical")

def Alpha(value):
    """
    Only alphabetical characters
    """
    if value.isalpha():
        return value
    else:
        raise ValidatorException(value, "Alphabetical")

def Date(value):
    """
    Checks the date format
    """
    if value.strftime("%Y-%m-%d"):
        return value
    else:
        raise ValidatorException(value, "Date")

def DateTime(value):
    """
    Checks the datetime format
    """
    if value.strftime("%Y-%m-%d"):
        return value
    else:
        raise ValidatorException(value, "DateTime")

def Digits(value):
    """
    Only digits
    """
    if value.isdigit():
        return value
    else:
        raise ValidatorException(value, "Digit")

def Email(value):
    """
    Checks the email format
    """
    pass

def Float(self, value):
    """
    Only float values
    """
    pass

def Hex(self, value):
    """
    Only hexadecimal characters
    """
    pass

def Hostname(self, value):
    """
    Checks the hostname format
    """
    pass

def Ip(self, value):
    """
    Checks the IP format
    """
    pass