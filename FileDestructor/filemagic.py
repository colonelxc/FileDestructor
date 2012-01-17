import magic

def filemagic(data):

    m = magic.Magic()
    return m.from_buffer(data)

