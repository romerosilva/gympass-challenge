import sys
import os

def main(argv=[]):
    usage = 'Usage: kart_analytics.py <path-to-file>'
    if len(argv) == 0:
        print(usage)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
