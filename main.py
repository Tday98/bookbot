from stats import print_stats
import sys

def main():
    """
    main.py

    Usage:
        python3 main.py <input_file>

    Arguments:
        input_file      Path to the input file
    """
    try:
        book_path = sys.argv[1]
        print(print_stats(book_path))
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()