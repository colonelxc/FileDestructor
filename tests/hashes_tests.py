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

def test_sha256():
    assert_equal(hashes.hash('sha256', teststringA), 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78')
    assert_equal(hashes.hash('sha256', teststringB), '8617dd494542bfb8766fad9553cef3f850332c7d04e1d8b2a826dc17a072e512')
    assert_equal(hashes.hash('sha256', teststringC), 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

def test_sha512():
    assert_equal(hashes.hash('sha512', teststringA), '397118fdac8d83ad98813c50759c85b8c47565d8268bf10da483153b747a74743a58a90e85aa9f705ce6984ffc128db567489817e4092d050d8a1cc596ddc119')
    assert_equal(hashes.hash('sha512', teststringB), 'd35d3ae9c849a8c653af4f855a3a306194a7efb310af870bcacfb738974c69a614d2e0a5621974185c7d648aeb14a7bcc6a4e6794ffbea6cbd8cdfaede52eb46')
    assert_equal(hashes.hash('sha512', teststringC), 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e')

