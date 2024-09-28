# DesignShift

## A Tool for Moving Architecture Diagrams between formats

April 2024 (See ChatGPT)

A collection of tools for converting Architecture formats. Allows the use of PowerPoint as an entry tool that can then be converted to standard tools, like C4 and Structurizr.

### Overview
This application leverages the EasyOCR library to perform text recognition on images. It is designed to quickly and accurately extract text from various image formats, supporting multiple languages.

### Installation
Before you can run this application, you'll need to install the required Python libraries. This project requires Python 3.6 or higher.

### Prerequisites
- Python 3.11+

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
pip install PyQt5
```

### Usage

To use this application, follow these steps:

Clone this repository or download the source code.
Place your image files in the images directory (you need to create this directory in the project root).
Run the script using the following command:
```bash
python DesignShift.py
```
The code will attempt to recognized text and other objects from one format to another. 
If you want to process multiple files or use different languages, modify the text_recognition.py script accordingly.

There's a few expermental code components: like a GUI builder, and an Antlr4 grammar for Structurizr, and a 
more generic version for DesignShift,

### Example Code

Here's a quick snippet from the DesignShift.py:

```python
import os

from ShiftPdf import convert_pdf_to_png
from ShiftPowerpoint import ppt_extraction
from ShiftStructurizr import parse_structurizr
from ShiftArchi import build_archi_xml
from pathlib import Path
DOWNLOADS_PATH = str(Path.home() / "Downloads")
INCOMING_PATH = "./incoming"
OUTGOING_PATH = "./outgoing"


if __name__ == "__main__":
    my_pdf_file = 'ems-color-system-diagram.pdf'
    convert_pdf_to_png(f'{INCOMING_PATH}/{my_pdf_file}')
    run_directory = os.getcwd()
    # slide_path = "US Electric GIS_Strategy_v01_debrief_11_21_22_summary.pptx
    # slide_path = "PI Facilitation Pack March 2024 Plan. Work Execution v2.pptx"
    structurizer_file = './dsl/amazon.dsl'
    parse_structurizr(structurizer_file)
    slide_path = f"{INCOMING_PATH}/connection.pptx"
    print(f"Processing '{slide_path}'")
    ppt_extraction(slide_path)

```

Replace `my_pdf_file` with the file name to convert. Place the incoming file in the incoming directory. 

Conversion is available for all these formats:

|                 | **PDF** | **PPTX** | **Archi** | **Structurizr** | **PNG** | **JSON** |
|-----------------|---------|----------|-----------|-----------------|---------|----------|
| **PDF**         |         | ->       |           |                 | ->      |          |
| **PPTX**        |         |          |           |                 |         | ->       |
| **Archi**       |         |          |           |                 |         | ->       |
| **Structurizr** |         | ->       |           |                 |         | ->       |
| **PNG**         | ->      | ->       |           |                 |         |          |
| **JSON**        |         | ->       | ->        | ->              |         |          |

A `->` entry in the table indicates a conversion path from that row type to that column type.

This is an imcomplete set of work. Mostly focuses on PPTX <-> JSON conversion. 

### Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your features or fixes.

### Support

If you encounter any problems or have any queries regarding the application, please open an issue in the repository.

### License

This project is licensed under the BSD 3-Clause License - see the LICENSE file for details.

