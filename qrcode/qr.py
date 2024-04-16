import qrcode
import cv2
from pyzbar.pyzbar import decode

# Fonction pour générer un QR Code avec les informations spécifiées
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Fonction pour scanner un QR Code à partir d'une image
def scan_qr_code(image_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray_img)
    if decoded_objects:
        for obj in decoded_objects:
            print('QR Code data:', obj.data.decode('utf-8'))

# Exemple d'utilisation : génération d'un QR Code avec des informations d'identification
object_info = {
    'client_id': 'ABC123',
    'transporter_id': 'XYZ789',
    'object_id': '12345'
}
qr_data = ','.join([f"{key}:{value}" for key, value in object_info.items()])
qr_image = generate_qr_code(qr_data)
qr_image.save('object_qr_code.png')

# Exemple d'utilisation : scanner un QR Code à partir d'une image
scan_qr_code('object_qr_code.png')
