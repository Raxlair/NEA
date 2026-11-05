from PIL import Image
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
    croppedPath = f'images/cropped images/croppedImage{screenshot.pictureCouter()}.png'
    croppedImage.save(croppedPath)
    croppedImage.show()
    return croppedPath

def OCR(imagePath):
    image = Image.open(imagePath)
    image.show()
    imagePath = cropImage(imagePath, (100, 500, 1200, 700))
    sentence = ocr.predict(imagePath)
    print(sentence)

OCR('images/screenshot12.png')
