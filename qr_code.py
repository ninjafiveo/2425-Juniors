import qrcode
import uuid
import os

def generate_qr_code(url, folder='qr_codes'):
    # Create a folder to save QR codes if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Generate a unique filename using uuid
    filename = f"{uuid.uuid4()}.png"
    
    # Create a QR code for the given URL
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image in the specified folder with a unique filename
    file_path = os.path.join(folder, filename)
    img.save(file_path)
    
    print(f"QR code saved as {file_path}")

# Example usage
url = input("Enter the website URL: ")
generate_qr_code(url)
