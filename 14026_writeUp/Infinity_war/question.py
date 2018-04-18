from hashlib import md5


def power(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]


def val(hl, m, hr):
    return power(hl, m), power(hr, m)


def AHash(hl, hr, M):
    message = list(map(''.join, zip(*[iter(M)] * 4)))
    for m in message:
        hl, hr = val(hl, m, hr)
        print hl
        print hr
    # return hl + hr
    print hl+hr

AHash('0001', 'bb9b', '1c4e72f08a807e49')
