# Python program to find the hash of a file

import hashlib

BUF_SIZE = 65536  # lets read stuff in 64kb which can be useful when trying to find the hash of large files as it saves memory

sha256 = hashlib.sha256() #The reason for using sha256 is to lower the possibility of a hash collision occuring when performing a hash lookup.
def hash_function(filepath):
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()