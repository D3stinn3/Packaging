"""Entry Point Script"""
import sys
from messo import message


message.word("".join(sys.argv[1:]))
