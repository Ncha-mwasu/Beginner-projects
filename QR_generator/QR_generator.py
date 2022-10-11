#!/usr/bin/python3
import qrcode
print("makes a QR code for a given input")
qr_input = str(input("Input message: "))
qr_gen = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4
)

qr_gen.add_data(qr_gen)
qr_gen.make(fit=True)
qr_img = qr_gen.make_image(fill_color = "cyan", back_color = "black")
qr_img.save("qr_project.png")
