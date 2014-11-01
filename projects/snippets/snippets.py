import logging
import csv
import argparse
import sys

def make_parser():
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)
    return parser

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file")
        writer.writerow([name, snippet])
    logging.debug("Write successful")
    return name, snippet

def main():
    logging.info("starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()
