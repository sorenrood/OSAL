# https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk

from PIL import Image
import pytesseract
import enchant

# Get text from image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('pic.jpg'))

# Make dictionary checker and list to add true words to
d = enchant.Dict("en_US")
words = []

# Split all words, check words, append to words if real word
for word in text.split(' '):
    if d.check(word):
        words.append(word)
    else:
        continue

# Print all real words
for word in words:
    print(word)