from nose.tools import *
from FileDestructor import hashes

from StringIO import StringIO

teststringA = 'ABC'
teststringB = 'ABCDEFG1234567'
teststringC = ''

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_md5():

    assert_equal(hashes.hash('md5', teststringA), '902fbdd2b1df0c4f70b4a5d23525e932')
    assert_equal(hashes.hash('md5', teststringB), 'ab9a4efbc060ec67fb775a622dfa5bfb')
    assert_equal(hashes.hash('md5', teststringC), 'd41d8cd98f00b204e9800998ecf8427e')
    
def test_sha1():

    assert_equal(hashes.hash('sha1', teststringA), '3c01bdbb26f358bab27f267924aa2c9a03fcfdb8')
    assert_equal(hashes.hash('sha1', teststringB), '1a25d711fa2f0471c4c8ae91641081cc760cbffe')
    assert_equal(hashes.hash('sha1', teststringC), 'da39a3ee5e6b4b0d3255bfef95601890afd80709')

