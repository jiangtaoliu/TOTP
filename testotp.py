import pyotp
str = "jet.lau@gmail.comHDECHALLENGE003"
#str = "JSXILTMMF2UAZ3NMFUWYLTDN5WUQRCFINEECTCMIVHEORJQGAZQ===="
#str = str.replace('\x00', '')
#str = str.encode('latin-1').decode('utf-16le')
print(str)
totp = pyotp.TOTP(str)

print("Current OTP:", totp.now())
