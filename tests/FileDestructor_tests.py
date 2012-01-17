from nose.tools import *
from FileDestructor import FileDestructor 

from StringIO import StringIO

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_output():

    testlist = [('a','b'),('c','d')]
   
    #test text option
    out = StringIO()
    FileDestructor.output('text', testlist, out)
    output = out.getvalue().strip()
    assert_equal( output, "a: b\nc: d")

    #test json option
    out = StringIO()
    FileDestructor.output('json', testlist, out)
    output = out.getvalue().strip()
    assert_equal( output, '{"a": "b", "c": "d"}')

    #test invalid output option
    assert_equal( FileDestructor.output('blah', testlist), 1)

    #test empty output
    assert_equal( FileDestructor.output('text', None), 1)
    assert_equal( FileDestructor.output('text', list()), 1)

