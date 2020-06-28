import qrcode
from PIL import Image

img = qrcode.make('Name is C wiz. I am a Developer. Address is Localhost. Skill is Nob.')

print(type(img))
print(img.size)

img.save('1.png')
