"""Entry Point Script"""
import sys
from messo import message

def main():
    message.word("".join(sys.argv[1:]))

if __name__ == "__main__":
       main()
