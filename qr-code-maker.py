import pyqrcode
import png


def qr_code():
    s = 'https://drive.google.com/file/d/1g77JlbU2GaSQNaRm3YC8QVIuNW-EzU-k/view?usp=drivesdk'
    d = pyqrcode.create(s)
    d.png('image.png', scale=6)  # inbuilt dunction for qrcode object
    print("Code execution successful")


if __name__ == '__main__':
    qr_code()
