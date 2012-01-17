#! /usr/bin/env python

import argparse
import sys
import simplejson

import hashes

ver = 0.1

def main():

    args = process_args()

    data = args.file.read()
    args.file.close()


    results = dict()
    if args.md5 or args.all:
        results["md5"] = hashes.md5(data)
    if args.sha1 or args.all:
        results["sha1"] = hashes.sha1(data)


    output(args.output, results)

    return 0


# Use argparse to evaluate the command line arguments
def process_args():
    global ver

    parser = argparse.ArgumentParser(description='Generate metadata for a file', prog='FileDestructor')
    parser.add_argument('-f', '--file', type=argparse.FileType('rb'), required=True)
    parser.add_argument('--version', action='version', version="%(prog)s " + str(ver))

    #Tool options
    parser.add_argument('-a', '--all', action='store_true', help='Run all tools')
    parser.add_argument('--md5', action='store_true', help='MD5 hash of the file')
    parser.add_argument('--sha1', action='store_true', help='SHA1 hash of the file')
    
    
    #print option 
    parser.add_argument('--output', choices=['text','json'], default='text', help='Print in either a simple text format (default) or json')

    args = parser.parse_args()

    return args



#print out the results
def output(format, results, out=sys.stdout):

    if results is None or len(results) == 0:
        return 1

    if format == 'text':
        text_output(results, out)
    elif format == 'json':
        json_output(results, out)
    else:
        #shouldn't get here
        return 1

    return 0

def json_output(results, out=sys.stdout):
    out.write(simplejson.dumps(results))
    out.write('\n')

def text_output(results, out=sys.stdout):
    for elem in results:
        out.write("%s: %s\n" % (elem, results[elem]))

if __name__ == '__main__':
    sys.exit(main())

