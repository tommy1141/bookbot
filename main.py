import sys
from stats import *
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    input_file = sys.argv[1]
    print(report(input_file))
main()