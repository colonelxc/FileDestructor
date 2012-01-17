from nose.tools import *
from FileDestructor import filemagic



def test_magic():
    assert_equal(filemagic.filemagic(''),'empty')
    assert_equal(filemagic.filemagic('%PDF-1.4\n'),'PDF document, version 1.4')
    
