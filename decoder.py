from PIL import Image
import random
import os

cleprivee="pop"
alphabet = "abcdefghijklmnopqrstuvwxyz. ABCDEFGHIJKLMNOPQRSTUVWXYZ,_\"\#\'&$%)(!?*+-/0123456789][:;@=><|}{~^¨`€°éèàùç"

image=Image.open(os.path.join('random_image.png'))

def melanger_alphabet_selon_cle(cle,alphabet):
    alphabet = list(alphabet)
    random.seed(cle)  # Initialiser la graine pour assurer la reproductibilité
    random.shuffle(alphabet)
    return ''.join(alphabet)

alphabet=melanger_alphabet_selon_cle(cleprivee,alphabet)
# Afficher la liste de caractères de l'alphabet arrangée de manière désordonnée
print("Liste de caractères de l'alphabet arrangée de manière désordonnée :", alphabet)

def test_image(image):
    w,h = image.size
    cnt=0
    for x in range(w):
        for y in range(h):
            colorcode = image.getpixel((x,y))
            if colorcode[0]==colorcode[1]==colorcode[2]:
                image.putpixel((x,y),(255,0,0))
                cnt+=1
    print(cnt)
    return(image)

def decode(image,alphabet):
    message=""
    w,h = image.size
    pixel_colors = []
    w,h = image.size
    for x in range(w):
        for y in range(h):
            colorcode= image.getpixel((x,y))
            if colorcode[0]==colorcode[1]==colorcode[2]:
                pixel_colors.append(colorcode)
    for i, color in enumerate(pixel_colors):
        if color[0]==color[1]==color[2]:
            message=''.join([message, (alphabet[color[0]])])
    return message

print(decode(image,alphabet))
test_image(image)
image.save("random_image.png")
with Image.open("random_image.png") as im:
    im.rotate(0).show()
