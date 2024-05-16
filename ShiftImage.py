# importing required modules
from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream, tree

import json
from datetime import datetime
from math import floor
import lxml.etree as etree

from PyPDF2 import PdfReader
from pdf2image import convert_from_path

from ShiftPdf import convert_pdf_to_png
from ShiftPowerpoint import ppt_extraction
from ShiftStructurizr import parse_structurizr
from ShiftArchi import build_archi_xml
from gen.StructurizrLexer import StructurizrLexer
from gen.StructurizrListener import StructurizrListener
from gen.StructurizrParser import StructurizrParser
from pptx import Presentation
from MsoShapeList import MSO_AUTO_SHAPE_TYPE_DICT, MSO_SHAPE_TYPE_DICT
# from pptx.enum.shapes import MSO_SHAPE
import numpy as np
import cv2
from pptx.enum.shapes import MSO_SHAPE_TYPE
from spire.presentation.common import *
from spire.presentation import Presentation as ShapePresentation, ISmartArt
from PIL import Image

import pypdfium2 as pdfium

import easyocr

from pathlib import Path
DOWNLOADS_PATH = str(Path.home() / "Downloads")

import logging
logger = logging.getLogger(__name__)




# First time run will download the english recognizer data set.
# You should get a message like:
# Downloading detection model, please wait. This may take several minutes depending upon your network connection.
# Progress: |██████████████████████████████████████████████████| 100.0% Complete
# Progress: |██████████████████████████████████████████████████| 100.0% Complete

reader = easyocr.Reader(['en'])

global tracker_image, gray_img, rotated_image


def on_shape_trackbar(detection_threshold):
    """
    Used with cv2 to help adjust the image detection thresholds
    :param val:
    :return:
    """
    global tracker_image, gray_img
    img = tracker_image.copy()
    # thickness = 5
    thickness = 1
    # fontscale = 0.5
    fontscale = 1.0
    # detection_threshold = 240
    # detection_threshold = 250
    threshold_type = cv2.THRESH_BINARY
    # threshold_type = cv2.THRESH_OTSU

    ret, thrash = cv2.threshold(gray_img, detection_threshold, 255, threshold_type)
    # retrieval_mode = cv2.RETR_LIST  # Retrieves all the contours without establishing any hierarchical relationships.
    retrieval_mode = cv2.RETR_TREE
    # retrieval_mode = cv2.RETR_EXTERNAL  # Retrieves only the extreme outer contours.
    # chain_method_type = cv2.CHAIN_APPROX_SIMPLE
    chain_method_type = cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv2.findContours(thrash, retrieval_mode, chain_method_type)

    for contour in contours:
        epsilon = 0.005 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), thickness)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            type = "TRIANGLE"
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            logger.info(f"Aspect ratio of this 4 sided item at {(x, y, w, h)} is {aspectRatio}")
            if 0.95 <= aspectRatio < 1.05:
                type = "SQUARE"
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            else:
                type = "RECTANGLE"
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y, w, h)}")

        elif len(approx) == 5:
            type = "PENTAGON"
            cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")

        elif len(approx) == 10:
            type = "STAR"
            cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")
        else:
            type = "CIRCLE"
            cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")
    cv2.imshow('shapes', img)

def image_shape_extract_tracker(png_file):
    # Load your image
    global tracker_image, gray_img
    tracker_image = cv2.imread(png_file)  # Make sure to provide the correct path
    gray_img = cv2.cvtColor(tracker_image, cv2.COLOR_BGR2GRAY)

    # Create a window and a trackbar
    cv2.namedWindow('shapes')
    cv2.createTrackbar('Threshold', 'shapes', 170, 255, on_shape_trackbar)

    # Initialize with a default value
    on_shape_trackbar(170)

    # Display the window until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

def image_shape_extract(png_file):

    img = cv2.imread(png_file)
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #thickness = 5
    thickness = 2
    # fontscale = 0.5
    fontscale = 1.0
    # detection_threshold = 240
    detection_threshold = 250
    # threshold_type = cv2.THRESH_BINARY
    threshold_type = cv2.THRESH_OTSU

    ret, thrash = cv2.threshold(imgGry, detection_threshold , 255, threshold_type)
    # retrieval_mode = cv2.RETR_LIST  # Retrieves all the contours without establishing any hierarchical relationships.
    retrieval_mode = cv2.RETR_TREE
    # retrieval_mode = cv2.RETR_EXTERNAL  # Retrieves only the extreme outer contours.
    # chain_method_type = cv2.CHAIN_APPROX_SIMPLE
    chain_method_type = cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv2.findContours(thrash, retrieval_mode, chain_method_type)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), thickness)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            type = "TRIANGLE"
            cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0) )
            logger.info(f"Found a {type} at {(x, y)}")
        elif len(approx) == 4 :
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            logger.info(f"Aspect ratio of this 4 sided item at {(x, y, w, h)} is {aspectRatio}")
            if 0.95 <= aspectRatio < 1.05:
                type = "SQUARE"
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            else:
                type = "RECTANGLE"
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y, w, h)}")

        elif len(approx) == 5 :
            type = "PENTAGON"
            cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")

        elif len(approx) == 10 :
            type = "STAR"
            cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")
        else:
            type = "CIRCLE"
            cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, fontscale, (0, 0, 0))
            logger.info(f"Found a {type} at {(x, y)}")

    cv2.imwrite(png_file+'.bmp', img)
    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return len(contours)
