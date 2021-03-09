# Ocular Sentiment Analysis Library (OSAL)

### Data and Analysis
https://docs.google.com/spreadsheets/d/1l6W0ZAt07hTXK2RLXPNIIMlB-2qxUbGGUxFAmiurOZo/edit?usp=sharing

### General Flow
1. Input Image (.jpg or .png) (run program by calling `python main.py data/path_to_input_image.jpg`)
2. Tesseract-OCR Convert Image to Text (Takes 10-15 seconds on my machine)
3. Clean Response (< 1 second)
4. Azure Text Sentiment Analysis (< 3 seconds)
5. Repeat
