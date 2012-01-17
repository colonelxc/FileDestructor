# Methods to perform hashes on the file
import hashlib

def hash(hashtype, data):
    hashtypes = set(['md5','sha1','sha256','sha512'])

    if data is None:
        data = ''

    if hashtype in hashtypes:
        digest = hashlib.new(hashtype)
        digest.update(data)
        return digest.hexdigest()
    else:
        return "Invalid hash type"
