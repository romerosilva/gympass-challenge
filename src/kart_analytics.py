import sys
import os

def main(argv=[]):
    usage = 'Usage: kart_analytics.py <path-to-file>'
    if len(argv) == 0:
        print(usage)
        sys.exit(1)

    if len(argv) > 1:
        print('ERROR: Multiple arguments provided.')
        print(usage)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
