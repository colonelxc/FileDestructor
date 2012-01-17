# Methods to perform hashes on the file
import hashlib

def md5(data):
    md5 = hashlib.md5()
    md5.update(data)

    return md5.hexdigest()


def sha1(data):
    sha1 = hashlib.sha1()
    sha1.update(data)

    return sha1.hexdigest()
    
