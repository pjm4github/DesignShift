# importing required modules
import os

from ShiftPdf import convert_pdf_to_png
from ShiftPowerpoint import ppt_extraction
from ShiftStructurizr import parse_structurizr
from ShiftArchi import build_archi_xml
from pathlib import Path

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
DOWNLOADS_PATH = str(Path.home() / "Downloads")
INCOMING_PATH = "./incoming"
OUTGOING_PATH = "./outgoing"


if __name__ == "__main__":
    convert_pdf_to_png(f'{INCOMING_PATH}/ems-color-system-diagram.pdf')
    run_directory = os.getcwd()
    # slide_path = "US Electric GIS_Strategy_v01_debrief_11_21_22_summary.pptx
    # slide_path = "PI Facilitation Pack March 2024 Plan. Work Execution v2.pptx"
    structurizer_file = './dsl/amazon.dsl'
    parse_structurizr(structurizer_file)
    slide_path = f"{INCOMING_PATH}/connection.pptx"
    print(f"Processing '{slide_path}'")
    ppt_extraction(slide_path)
