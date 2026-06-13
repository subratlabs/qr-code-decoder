import cv2

img = cv2.imread("qrcode.png")

detector = cv2.QRCodeDetector()

data, bbox, _ = detector.detectAndDecode(img)

#data means the text stored in the qr code and bbox means position od the qr code and _ means extra information (ignored)

if data:
    print("QR Code Data:", data)

else:
    print("No QR code found")    