import pyotp
str = "testpyotp"
#str = str.replace('\x00', '')
#str = str.encode('latin-1').decode('utf-16le')
print(str)
totp = pyotp.TOTP(str)

print("Current OTP:", totp.now())
