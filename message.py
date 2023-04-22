"""Script Bearing Message Written in Functions"""

from dotenv import load_dotenv
import os

"""Loading Message as Environment variable"""
load_dotenv()

MESSAGE = r"""Provided by d3$tinn3
    d3$tinn3 Copyright
"""

def bubble(message):
    bubble_length = len(message) * 2
    return f"""{"_" * bubble_length} ({message}) {"-" * bubble_length}"""

def word(message):
    print(bubble(message))
    print(MESSAGE)
    
    