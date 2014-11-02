import logging
import csv
import argparse
import sys

def make_parser():
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")

    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")

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

def get(name, filename):
    logging.info("Reading {!r} from {!r}".format(name, filename))
    logging.debug("Reading file")
    result = "This snippet name is nonexistent."
    with open(filename, "r") as f:
        reader = csv.reader(f)
        logging.debug("Reading snippet from file")
        flag = False
        for a,b in reader:
            if a == name:
                result = b
                logging.debug("Read successful")
                flag = True
                break
        if not flag:
            logging.debug("Read unsuccessful")
    return name, result

def main():
    logging.info("starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])

    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}".format(snippet, name)

    if command == "get":
        name, snippet = get(**arguments)
        print "Retrieved {!r}: {!r}".format(name, snippet)

if __name__ == "__main__":
    main()
