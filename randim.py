import random
import os
from PIL import Image

MESSAGE="Cet ordi me remplit de joie !"
CLE="pop"

image=Image.open(os.path.join('TF2.png'))

# Liste de caractères de l'alphabet limitée à cause de notre système à 256,
# n'importe quel alphabet peut être inséré et agir comme une impasse supplémentaire, ainsi qu'un adaptation à tous les langages.
ALPHABET="abcdefghijklmnopqrstuvwxyz. ABCDEFGHIJKLMNOPQRSTUVWXYZ,_\"\#\'&$%)(!?*+-/0123456789][:;@=><|}{~^¨`€°éèàùç"

def melanger_alphabet_selon_cle(cle, charlist):
    alphabet = list(charlist)
    random.seed(cle)  # Initialiser la graine pour assurer la reproductibilité
    random.shuffle(alphabet)
    return ''.join(alphabet)

alphabet = melanger_alphabet_selon_cle(CLE, ALPHABET)

# Afficher la liste de caractères de l'alphabet arrangée de manière désordonnée
print("Liste de caractères de l'alphabet arrangée de manière désordonnée :", alphabet)

def encoded_color(message, alpha):
    RGBcode=0
    for count in range(len(alpha)) :
        if alpha[count] == message:
            RGBcode=count
    return (RGBcode,RGBcode,RGBcode)

def encode_message(message):
    codelist=[]
    for i in range(len(message)):
        codelist.append(encoded_color(message[i], alphabet))
    return codelist

def prepare_image(image, messcode, tolerance=10):
    codelist = messcode
    found_rgb = set()  # Pour garder une trace des codes RGB trouvés
    w, h = image.size
    for x in range(w):
        for y in range(h):
            colorcode = image.getpixel((x, y))
            max_diff=max(colorcode)-min(colorcode)
            if colorcode[0] == colorcode[1] == colorcode[2] or max_diff<tolerance: 
                if codelist and colorcode==codelist[0]:
                        codelist.pop(0)
                else:
                        if colorcode[2]<128: # Transformer en bleu la couleur primaire la moins visible des trois
                            image.putpixel((x, y), (colorcode[0],colorcode[1],colorcode[2]+tolerance))
                        else:
                            image.putpixel((x, y), (colorcode[0],colorcode[1],colorcode[2]-tolerance))

    return image

def test_image(image):
    w,h = image.size
    cnt=0
    for x in range(w):
        for y in range(h):
            colorcode = image.getpixel((x,y))
            if colorcode[0]==colorcode[1]==colorcode[2]:
                cnt+=1
    return(cnt)
               

prepare_image(image,encode_message(MESSAGE))
image.save("random_image.png")
print("Image générée avec succès.")
with Image.open("random_image.png") as im:
    im.rotate(0).show()


