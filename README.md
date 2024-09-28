# DesignShift

April 2024 (See ChatGPT)

A collection of tools for expressing design ideas. 

# Text Recognition Application

## Overview
This application leverages the EasyOCR library to perform text recognition on images. It is designed to quickly and accurately extract text from various image formats, supporting multiple languages.

## Installation

Before you can run this application, you'll need to install the required Python libraries. This project requires Python 3.6 or higher.

### Prerequisites
- Python 3.6+
- pip

### Libraries
Install the following Python library using pip:

```bash
pip install pandas~=2.2.2
pip install PyPDF2~=3.0.1
pip install pillow~=10.3.0
pip install python-pptx
# pytesseract
pip install Spire.Presentation
pip install easyocr~=1.7.1
pip install lxml~=5.2.1
pip install opencv-python~=4.9.0.80
pip install pymupdf
pip install pypdfium2~=4.29.0
pip install antlr4-python3-runtime
pip install pdf2image~=1.17.0
pip install numpy~=1.26.4
pip install PyYAML~=6.0.1
```


### Usage

To use this application, follow these steps:

Clone this repository or download the source code.
Place your image files in the images directory (you need to create this directory in the project root).
Run the script using the following command:
```bash
python DesignShift.py
```
The script will output the recognized text directly in the terminal. If you want to process multiple files or use different languages, modify the text_recognition.py script accordingly.

### Example Code

Here's a quick snippet from the text_recognition.py:

```python
import easyocr

def recognize_text(image_path):
    reader = easyocr.Reader(['en'])  # For English
    results = reader.readtext(image_path)
    for result in results:
        print(result[1])  # Outputs the recognized text

if __name__ == '__main__':
    image_path = 'path_to_your_image.jpg'
    recognize_text(image_path)
```

Replace 'path_to_your_image.jpg' with the path to your actual image.

### Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your features or fixes.

### Support

If you encounter any problems or have any queries regarding the application, please open an issue in the repository.

### License

This project is licensed under the MIT License - see the LICENSE file for details.


