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
    return croppedPath

def OCR(imagePath, textBox):
    sentence = ''
    image = Image.open(imagePath)
    imagePath = cropImage(imagePath, textBox)
    result = ocr.predict(imagePath)
    for line in result[0]['rec_texts']: #allows for multple line of text to be store in variable sentnce
        sentence = sentence + line
    return sentence
