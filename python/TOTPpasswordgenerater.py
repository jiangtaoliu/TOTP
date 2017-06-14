#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a key, generate a HMAC-Based (HOTP) or Time-based One-Time Password
(TOTP) (see RFC 4226 and 6238).
"""
import base64
import hashlib
import hmac
import struct
import sys
import time


#def hotp(key, counter):
#    counter_bytes = struct.pack(b'>Q', counter)
#    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).hexdigest()
#    offset = int(hmac_hash[-1], 16)
#    value = int(hmac_hash[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
#    return str(value)[-6:]
#
#
#def totp(key, counter=None, time_step=30):
#    counter = long(time.time() / time_step)
#    return hotp(key, counter)


def hotp(secret, count):
    print("====================")
    print(secret)
    print(count)
    print("====================")
    data = bytearray([int(hex(count >> i & 0xff), 16) for i in (56, 48, 40, 32 ,24, 16, 8, 0)])
    hs = hmac.new(secret, data, hashlib.sha512).hexdigest()
    offset = int(hs[-1], 16)
    sbits = int(hs[offset * 2: offset * 2 + 8], 16) & 0x7fffffff
    return sbits % 1000000


# jet.lau@gmail.comHDECHALLENGE003
def totp(secret, unix_time):
    return hotp(secret, int(unix_time))


if __name__ == '__main__':
    usage_msg = 'Usage: {} (hotp|totp) <secret> [counter]'.format(sys.argv[0])

    try:
        if len(sys.argv) < 3:
            raise RuntimeError(usage_msg)
        kind = sys.argv[1]
        try:
            counter = long(sys.argv[3])
        except IndexError:
            if kind == 'hotp':
                raise RuntimeError(usage_msg)
            counter = None
        except ValueError:
            raise RuntimeError('{}: Invalid counter.'.format(sys.argv[0]))
        try:
            secret = sys.argv[2]
            #key = base64.b32encode(secret, casefold=True)
            key = "JSXILTMMF2UAZ3NMFUWYLTDN5WUQRCFINEECTCMIVHEORJQGAZQ===="
        except TypeError:
            print('{}: Invalid secret.'.format(sys.argv[0]))
            sys.exit(1)
        time_step=30
        counter = long(time.time() / time_step)
        print(secret)
        print(time.time())
        print(counter)

        code = {
            'hotp': hotp,
            'totp': totp
        }.get(kind)(key, counter)

        print(code)
    except RuntimeError as e:
        print(e.message)
        sys.exit(1)