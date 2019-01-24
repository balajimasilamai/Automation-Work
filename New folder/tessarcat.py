try:
    import Image
except ImportError:
    from PIL import Image
import C
abc=Image.open('1.jpg')
print(pytesseract.image_to_string(abc,lang='en'))
