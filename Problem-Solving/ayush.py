import qrcode

qr = qrcode.make("https://github.com/ayushripu")

qr.save("ayushQrcode.png")

print("Qrcode Generate Successfully. ")