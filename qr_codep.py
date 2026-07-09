import qrcode

url = input("Enter the URL: ").strip()
filepath = r"C:\\Users\\Jash Mistry\\Desktop\\qrcode.jpeg"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filepath)

print("QR code was generated successfully!")
