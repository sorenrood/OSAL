# https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk

from PIL import Image
import pytesseract
import enchant
import nltk

# Get text from image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('pic.jpg'))

# Make dictionary checker and list to add true words to
d = enchant.Dict("en_US")
words = []

# Clean Data
bad_chars = [';', ':', '!', "*", "|", "{", "}"]
cleaned = ''.join((filter(lambda i: i not in bad_chars, text)))
print(cleaned)

# Tokenizing (convert into sentences)
sentence_list = nltk.tokenize.sent_tokenize(cleaned)
for sentence in sentence_list:
    print('-----------------')
    print(sentence)
    print('-----------------')