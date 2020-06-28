# run နည်း # Usage
# python qrcodescan.py --image example.png

# လိုအပ်တဲ့ library တေ import လုပ် # import all necessary libraries
from pyzbar import pyzbar
import argparse
import cv2
from pyfiglet import Figlet

# just for beautiful text
custom_fig = Figlet(font='standard')

# argparse သုံးပီး input image တောင်း , ArgumentParser သုံးထားလို့ ဒီလို run ရ => $python qrcodescan.py --image example.png
# Request input image using argparse, so we can run in command like this => $python qrcodescan.py --image example.png
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# image ကို ယူ # Load image
image = cv2.imread(args["image"])

# image ထဲက QR code ကို ရှာပီး decode # find qrcodes in the image and decode them
qrcodes = pyzbar.decode(image)

# QR code ရှိသလောက် loop ပတ် # loop for all qr codes
for qrcode in qrcodes:

    # Image ထဲက QR code နေရာကို ရှာပီး စတုဂံ ဘောင်ကို ဆွဲ # find the location of qrcodes and draw rectangle boundary
	(x, y, w, h) = qrcode.rect
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # qrcode ကို စာသားအနေနဲ့ယူ # to get the decoded qrcodes as string
	qrcodeData = qrcode.data.decode("utf-8")
    # code အမျိုးအစား သိရန်  # to get types of code such as qrcode , barcode etc.
	qrcodeType = qrcode.type

    # ရလာတဲ့စာသားရှည်ရင် အောက်တကြောင်းဆင်းအောင် လျှောက်လုပ်ထား ပီး Image မှာ ရေး
    # doing a few steps to get endline for long string and draw this string on the image
	qrtrim = qrcodeData[:40]
	leftqr = qrcodeData.replace(qrtrim, '')
	lasttext = qrtrim + "\n"+ leftqr
	text = "{} ({})".format(lasttext, qrcodeType)
	y0, dy = 40, 13
	for i, line in enumerate(text.split('\n')):
		y = y0 + i*dy
		cv2.putText(image, line, (40, y - 30 ), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)


# output result show on terminal
print("[OUTPUT] Found {} QR code : {}".format(qrcodeType, text))
print(custom_fig.renderText('Done!'))

# image ပြ # show image
cv2.imshow("Image", image)
cv2.waitKey(0)
