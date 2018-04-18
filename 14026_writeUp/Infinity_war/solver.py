from hashlib import md5
# from fHash import power

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
    return hl + hr
    # print hl+hr

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
hl = 'd068'
hr = 'dedc'
msg = ''
for i in range(0, 4):
    cur = False
    for j in arr:
        if cur == True:
            break
        for k in arr:
            if cur == True:
                break
            for l in arr:
                if cur == True:
                    break
                for m in arr:
                    if cur == True:
                        break
                    for n in arr:
                        if cur == True:
                            break
                        for o in arr:
                            if cur == True:
                                break
                            for p in arr:
                                if cur == True:
                                    break
                                for q in arr:
                                    if cur == True:
                                        break
                                    hl_cur = j + k + l + m
                                    msg_cur = n + o + p + q
                                    if power(hl_cur, msg_cur) == hl:
                                        for r in arr:
                                            if cur == True:
                                                break
                                            for s in arr:
                                                if cur == True:
                                                    break
                                                for t in arr:
                                                    if cur == True:
                                                        break
                                                    for u in arr:
                                                        hr_cur = r + s + t +u
                                                        if power(hr_cur, msg_cur) == hr:
                                                            cur = True
                                                            msg = msg_cur + msg
                                                            hl = hl_cur
                                                            hr = hr_cur
                                                            print hl_cur, hr_cur, msg_cur
                                                            break
print(hl, hr, msg)