from PIL import Image, ImageDraw
from paddleocr import PaddleOCR
import screenshot

ocr = PaddleOCR( #initialising PaddleOCR
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

def cropImage(imagePath, imageCrop): #return the IMAGEPATH of the cropped image
    image = Image.open(imagePath)
    croppedImage = image.crop(imageCrop)
    croppedImage.save(f'images/cropped images/croppedImage{screenshot.pictureCouter()}.png')
    croppedImage.show()

def OCR(imagePath):
    image = Image.open(imagePath)
    image.show()
    sentence = ocr.predict(imagePath)
    print(sentence)

#OCR('images/screenshot3.png')

cropImage('images/screenshot3.png',(100, 500, 1200, 700))