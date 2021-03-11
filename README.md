# Ocular Sentiment Analysis Library (OSAL)

### Labeled Data
![data](https://cdn.discordapp.com/attachments/819467035578859541/819685526650486804/events-graph.jpg)

### Description
TODO

### Data and Analysis
* [Data Spreadsheet](https://docs.google.com/spreadsheets/d/1l6W0ZAt07hTXK2RLXPNIIMlB-2qxUbGGUxFAmiurOZo/edit?usp=sharing)

* Article Explaining Findings (not written yet)

### Setup
* [Install tesseract via pre-built binary package](https://tesseract-ocr.github.io/tessdoc/Home.html)
* Set up azure cognitive services resource and enable text analytics API.
* Configure variables for your machine on lines 14-17 in `main.py`

### General Program Flow
1. Run program by calling `python main.py data/path_to_input_image.jpg`
2. Tesseract-OCR Convert Image to Text (10-15 seconds on my machine)
3. Clean Response (< 1 second)
4. Azure Text Sentiment Analysis (< 3 seconds)
5. Repeat
