import pyqrcode
from pyqrcode import QRCode

s = "https://www.qwiklabs.com/public_profiles/eba69a44-2f64-4a17-b0b8-e554b47a4383"
url = pyqrcode.create(s)
url.svg("myqwiklabs.svg", scale=8)