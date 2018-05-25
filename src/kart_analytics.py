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

    try:
        if os.path.isfile(argv[0]):
            print('true')

        else:
            raise Exception('Unexpected program argument. Only file names are allowed.')

    except Exception as e:
        print('ERROR: {}'.format(e))
        sys.exit(3)

if __name__ == "__main__":
    main(sys.argv[1:])
