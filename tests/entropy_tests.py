from nose.tools import *
from FileDestructor import entropy

from StringIO import StringIO


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_entropy():

    #empty case
    assert_equal(entropy.entropy(''),0.0)
    #only one character case
    assert_equal(entropy.entropy('aaaaaaaaaaaaa'),0.0)

    #one of every possible byte
    s = str()
    for byte in range(0,256):
        s+= chr(byte)

    assert_equal(entropy.entropy(s), 8.0)

    #TODO: Add more exotic cases? Might be hard to use asserts since it is floating point math, possible errors...


