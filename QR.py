import qrcode

def generate_QR(text):
    qr=qrcode.QRCode(

        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
                       )
     

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save("qrimag.png")

url=input("please enter the URL you want to geneerate the QRcode for: ")
generate_QR(url)

