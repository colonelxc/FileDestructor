#! /usr/bin/env python

import argparse
import sys
import simplejson

#local project imports
import hashes
import entropy

ver = 0.1

def main():

    args = process_args()

    data = args.file.read()
    args.file.close()


    results = list()
    if args.md5 or args.all:
        results.append(('md5',hashes.hash('md5', data)))
    if args.sha1 or args.all:
        results.append(('sha1', hashes.hash('sha1', data)))

    if args.entropy or args.all:
        results.append(('entropy', entropy.entropy(data)))

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
    parser.add_argument('--entropy', action='store_true', help='Entropy of the bytes of the file')
    
    
    #print option 
    parser.add_argument('--output', choices=['text','json'], default='text', help='Print in either a simple text format (default) or json')

    args = parser.parse_args()

    return args



"""Print out the results.
Format is either 'text' or 'json'.
results is a list of 2-tuples, such as [('md5', 'abc...'),('sha1','def...')]"""
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
    print >>out, simplejson.dumps(dict(results))

def text_output(results, out=sys.stdout):
    for elem in results:
        print >>out, "%s: %s" % elem

if __name__ == '__main__':
    sys.exit(main())

