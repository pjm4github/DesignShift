# importing required modules
import csv
import json
import os
from datetime import datetime

from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pypdfium2 as pdfium
from pathlib import Path
import fitz  # PyMuPDF

import logging
logger = logging.getLogger(__name__)

int_to_rgb = lambda color_int: tuple(map(lambda x: (color_int >> (8 * x)) & 0xFF, [2, 1, 0]))

def pdf_extraction2(pdf_path):
    pdf_user_space_units_per_inch = 72
    emus_per_inch = 914400
    # Conversion factor from one PDF user space unit to EMUs
    conversion_factor = emus_per_inch / pdf_user_space_units_per_inch
    doc = fitz.open(pdf_path)
    # Extracting creation and modification dates
    author = doc.metadata['author']
    title = doc.metadata['title']
    subject = doc.metadata['subject']
    creator = doc.metadata['creator']
    producer = doc.metadata['producer']
    date_str = doc.metadata['creationDate']
    try:
        creation_date = datetime.strptime(date_str.replace("'", ""), "D:%Y%m%d%H%M%S%z").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        creation_date = date_str
    date_str = doc.metadata['modDate']
    try:
        modification_date = datetime.strptime(date_str.replace("'", ""), "D:%Y%m%d%H%M%S%z").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        modification_date = date_str

    number_of_pages = len(doc)
    # one for each text run in presentation
    prefix = datetime.now().strftime("Y%Ym%md%d-H%HM%MS%S")
    extract_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    output_path = f"./pdf/scan/{prefix}/"
    path_exists = os.path.exists(output_path)
    if not path_exists:
        # Create a new directory because it does not exist
        os.makedirs(output_path)
    logging.basicConfig(filename=f'{output_path}conversion.log', encoding='utf-8', level=logging.INFO)
    logging.info(f"Processing the pdf document {pdf_path}")
    logger.info(f"number of pages={number_of_pages}")

    meta_data = {"file": pdf_path,
                 "page count": number_of_pages,
                 "author": author,
                 "created on": f" {creation_date} UTC",
                 "modified on": f" {modification_date} UTC",
                 "extracted on": f" {extract_time} UTC",
                 "title": title,
                 "subject": subject,
                 "creator": creator,
                 "producer": producer,
                 }
    with open(f"{output_path}/meta-data.json", 'w') as f:
        f.write(json.dumps(meta_data, indent=4))

    all_blocks = []
    all_graphics = []
    text_layout = []
    text_flow = []
    for page_number, page in enumerate(doc):
        page_blocks = []
        page_graphics = []
        # Extract text by blocks
        output_path = f"./pdf/scan/{prefix}/page-{page_number + 1}"
        path_exists = os.path.exists(output_path)
        if not path_exists:
            # Create a new directory because it does not exist
            os.makedirs(output_path)
        # lines = page.get_text("line")

        blocks = page.get_text("dict")['blocks']
        for block in blocks:
            if 'lines' in block:  # Ensure the block contains lines of text
                for line in block['lines']:
                    for span in line['spans']:  # Each span should have font info
                        bounding_box = tuple(map(lambda x: int(x * conversion_factor), span.get('bbox'))) if span.get(
                            'bbox') else None
                        info = {
                            'text': span['text'],
                            'font': span['font'],  # Font name
                            'size': span['size'],  # Font size
                            'color': int_to_rgb(span['color']), # Font color (RGB tuple)
                            'flags': span['flags'],
                            "origin": tuple(map(lambda x: int(x * conversion_factor), span.get('origin'))) if span.get('origin') else None,
                            "bbox": bounding_box,
                            "ascender": span['ascender'],
                            "descender": span['descender'],
                        }
                        text_layout.append(info)
                        # x0: The x-coordinate of the left edge of the bounding box.
                        # y0: The y-coordinate of the top edge of the bounding box.
                        # x1: The x-coordinate of the right edge of the bounding box.
                        # y1: The y-coordinate of the bottom edge of the bounding box.
                        text_flow.append([page_number + 1, bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3], span['text']])

        # blocks = page.get_text("blocks")  # Each item in 'blocks' represents a block of text
        # for block in blocks:
        #     # block consists of: x0, y0, x1, y1, "text", block_no
        #     page_blocks.append({
        #         'page-number': page.number + 1,
        #         'x0': int(block[0] * conversion_factor),
        #         'y0': int(block[1] * conversion_factor),
        #         'x1': int(block[2] * conversion_factor),
        #         'y1': int(block[3] * conversion_factor),
        #         'text': block[4].strip()
        #     })

        with open(f"{output_path}/text-layout.json", 'w') as f:
            f.write(json.dumps({"page-number": page.number + 1,
                                "page-size":
                                    {"width": int(page.rect.width * conversion_factor),
                                     "height": int(page.rect.height * conversion_factor)},
                                "text-layout": text_layout}, indent=4))
        t6 = page.get_text()
        with open(f"{output_path}/page-text.txt", 'wb') as f:
            f.write(t6.encode('utf-8'))
        # all_blocks.append(page_blocks)

        all_blocks.append(text_layout)
        drawings = page.get_drawings()
        for item in drawings:
            # Types in the drawing:
            # "line": A simple line segment defined by its start and end points.
            # "spline": Typically a curve defined by multiple control points. It may not be explicitly listed in some documents but can represent Bézier curves and similar complex paths.
            # "polygon": A closed path defined by multiple line segments that form a boundary. It does not need to be filled.
            # "rectangle": A four-sided polygon with right-angle corners, often used for both filling and stroking.
            # "ellipse": Includes circles as well; defined by a bounding box and not necessarily by center point and radius.
            # "text": When text is treated graphically, it can be extracted as part of the drawing operations, especially in cases where text is outlined.
            # "image": Represents embedded images, which can be extracted as part of the graphic content.
            # "shading": Complex color and shading patterns that can include gradients or mesh-based color interpolations.
            # "form": Used for PDF form XObjects, which are reusable content objects; this can include nested drawings.
            # "f" (fill): Used when paths are filled without stroking.
            # "s" (stroke): Used when paths are stroked without filling.
            # "fs" or "sf": Used when paths are both filled and stroked, either could be used depending on the order of operations.
            # "clip": Not usually a visible operation but defines the clipping path for subsequent drawing operations.
            if item['type'] == 'fs':
                r = item.get('rect')
                if r:
                    rectangle = [int(r[0] * conversion_factor),
                                 int(r[1] * conversion_factor),
                                 int(r[2] * conversion_factor),
                                 int(r[3] * conversion_factor)]
                else:
                    rectangle = None
                nested_items = item.get('items')
                points = []
                if nested_items:
                    # for p in nested_items[:-1]:
                    #     if p[0] == 'l': # this is a point, startx, starty, stopx, stopy
                    #         points.append([int(p[1][0] * conversion_factor), int(p[1][1] * conversion_factor)])
                    # p = nested_items[-1]
                    # if p[0] == 'l':  # this is a point, startx, starty, stopx, stopy
                    #     points.append([int(p[2][0] * conversion_factor), int(p[2][1] * conversion_factor)])
                    # # points_string = ";".join(points)
                    for p in nested_items:
                        if p[0] == 'l': # this is a point, startx, starty, stopx, stopy
                            points.append([int(p[1][0] * conversion_factor), int(p[1][1] * conversion_factor),
                                           int(p[2][0] * conversion_factor), int(p[2][1] * conversion_factor)])

                graphic_details = {
                    'page-number': page.number + 1,
                    'type': item['type'],
                    'rectangle': rectangle,
                    'points': points,  # some drawings use 'rect', others 'points'
                    'fill-color': tuple(map(lambda x: int(x*255), item.get('fill_color'))) if item.get('fill_color') else None,
                    'stroke-color': tuple(map(lambda x: int(x * 255), item.get('stroke_color'))) if item.get('stroke_color') else None,
                    'color': tuple(map(lambda x: int(x * 255), item.get('color'))) if item.get('color') else None,
                    'width': item.get('width', None),  # Width of the stroke
                    'pattern': item.get('pattern', None)  # Pattern used, if any
                }
                page_graphics.append(graphic_details)

            elif item['type'] == 'line':
                graphic_details = {'page-number': page.number + 1,
                                   'type': item['type'],
                                   'points': item['rect'] if item['type'] == 'rect' else item['points'],
                                   'color': item['color'],
                                   'width': item['width']
                                   }
                page_graphics.append(graphic_details)

            elif item['type'] == 'rectangle':
                graphic_details = {'page-number': page.number + 1,
                                   'type': item['type'],
                                   'points': item['rect'] if item['type'] == 'rect' else item['points'],
                                   'color': item['color'],
                                   'width': item['width']
                                   }
                page_graphics.append(graphic_details)

            elif item['type'] == 's':
                r = item.get('rect')
                if r:
                    rectangle = [int(r[0] * conversion_factor),
                                 int(r[1] * conversion_factor),
                                 int(r[2] * conversion_factor),
                                 int(r[3] * conversion_factor)]
                else:
                    rectangle = None

                nested_items = item.get('items')
                quad_points = []
                if nested_items:
                    # for p in nested_items[:-1]:
                    #     if p[0] == 'l': # this is a point, startx, starty, stopx, stopy
                    #         points.append([int(p[1][0] * conversion_factor), int(p[1][1] * conversion_factor)])
                    # p = nested_items[-1]
                    # if p[0] == 'l':  # this is a point, startx, starty, stopx, stopy
                    #     points.append([int(p[2][0] * conversion_factor), int(p[2][1] * conversion_factor)])
                    # # points_string = ";".join(points)
                    for p in nested_items:
                        if p[0] == 'qu':  # this is a point, startx, starty, stopx, stopy
                            point_list = list(p[1])
                            for pl in point_list:
                                quad_points.append([int(pl[0] * conversion_factor) , int(pl[1] * conversion_factor)])

                graphic_details = {
                    'page-number': page.number + 1,
                    'type': item['type'],
                    'rectangle': rectangle,
                    'quads': quad_points,  # some drawings use 'rect', others 'points'
                    'fill-color': tuple(map(lambda x: int(x*255), item.get('fill_color'))) if item.get('fill_color') else None,
                    'stroke-color': tuple(map(lambda x: int(x * 255), item.get('stroke_color'))) if item.get('stroke_color') else None,
                    'color': tuple(map(lambda x: int(x * 255), item.get('color'))) if item.get('color') else None,
                    'width': item.get('width'),  # Width of the stroke
                    'pattern': item.get('pattern'),  # Pattern used, if any
                    'layer': item.get('layer'),
                    'seqno': item.get('seqno'),
                    'fill': tuple(map(lambda x: int(x * 255), item.get('fill'))) if item.get('fill') else None,
                    'fill-opacity': item.get('fill_opacity'),
                    'even-odd': item.get('even_odd'),
                    'stroke_opacity': item.get('stroke_opacity'),
                    'line-cap': item.get('lineCap'),
                    'line-join': item.get('lineJoin'),
                    'close-path': item.get('closePath'),
                    'dashes': item.get('dashes')
                }
                page_graphics.append(graphic_details)

                pass
            elif item['type'] == 'f':
                r = item.get('rect')
                if r:
                    rectangle = [int(r[0] * conversion_factor),
                                 int(r[1] * conversion_factor),
                                 int(r[2] * conversion_factor),
                                 int(r[3] * conversion_factor)]
                else:
                    rectangle = None

                nested_items = item.get('items')

                rect_points = []
                if nested_items:
                    # for p in nested_items[:-1]:
                    #     if p[0] == 'l': # this is a point, startx, starty, stopx, stopy
                    #         points.append([int(p[1][0] * conversion_factor), int(p[1][1] * conversion_factor)])
                    # p = nested_items[-1]
                    # if p[0] == 'l':  # this is a point, startx, starty, stopx, stopy
                    #     points.append([int(p[2][0] * conversion_factor), int(p[2][1] * conversion_factor)])
                    # # points_string = ";".join(points)
                    for p in nested_items:
                        if p[0] == 're':  # Rectangle
                            # given : Rect(355.25, 759.0, 544.5, 769.0)
                            # 355.25: The x-coordinate of the lower-left corner of the rectangle.
                            # 759.0: The y-coordinate of the lower-left corner of the rectangle.
                            # 544.5: The x-coordinate of the upper-right corner of the rectangle.
                            # 769.0: The y-coordinate of the upper-right corner of the rectangle.
                            # this is a point, startx, starty, stopx, stopy
                            pl = list(p[1])
                            rect_points = {"x0": int(pl[0] * conversion_factor),
                                           "y0": int(pl[1] * conversion_factor),
                                           "x1": int(pl[2] * conversion_factor),
                                           "y1": int(pl[3] * conversion_factor)}

                # {'items': [('re', Rect(355.25, 759.0, 544.5, 769.0), -1)],
                graphic_details = {
                    'page-number': page.number + 1,
                    'type': item['type'],
                   #  'rectangle': rectangle, # rectangle-corners are used for this
                    'rectangle-corners': rect_points,  # some drawings use 'rect', others 'points'
                    'fill-color': tuple(map(lambda x: int(x*255), item.get('fill_color'))) if item.get('fill_color') else None,
                    'stroke-color': tuple(map(lambda x: int(x * 255), item.get('stroke_color'))) if item.get('stroke_color') else None,
                    'color': tuple(map(lambda x: int(x * 255), item.get('color'))) if item.get('color') else None,
                    'width': item.get('width'),  # Width of the stroke
                    'pattern': item.get('pattern'),  # Pattern used, if any
                    'layer': item.get('layer'),
                    'seqno': item.get('seqno'),
                    'fill': tuple(map(lambda x: int(x * 255), item.get('fill'))) if item.get('fill') else None,
                    'fill-opacity': item.get('fill_opacity'),
                    'even-odd': item.get('even_odd'),
                    'stroke-opacity': item.get('stroke_opacity'),
                    'line-cap': item.get('lineCap'),
                    'line-join': item.get('lineJoin'),
                    'close-path': item.get('closePath'),
                    'dashes': item.get('dashes')
                }
                page_graphics.append(graphic_details)
            else:
                print(f"Unknown item type: {item['type']}")

        with open(f"{output_path}/page-graphics.json", 'w') as f:
            f.write(json.dumps({"graphics": page_graphics}, indent=4))
        all_graphics.append(page_graphics)

        pixmap = page.get_pixmap(dpi=200)
        pixmap.save(f"{output_path}/pixmap.png")

    document_text = json.dumps({'document_block_text': all_blocks}, indent=4)
    output_path = f"./pdf/scan/{prefix}"

    with open(f"{output_path}/joined.json", 'a', encoding="utf-8") as f:
        f.write(document_text)

    headers = ['page-number', 'x0', 'y0', 'x1', 'y1', 'text']

    # Open the file in write mode
    with open(f"{output_path}/joined.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(headers)
        # Write the data
        writer.writerows(text_flow)

    doc.close()

#
# # Example usage
# pdf_path = 'path_to_your_pdf.pdf'
# text_blocks = extract_text_blocks(pdf_path)
# for block in text_blocks:
#     print(f"Page {block['page_number']}: [{block['x0']}, {block['y0']}, {block['x1']}, {block['y1']}] - {block['text']}")
# Key Features of the Code:
# Text Extraction by Blocks: get_text("blocks") method retrieves text in blocks where each block includes coordinates and text content.
# Bounding Box: Each block contains a bounding box (x0, y0, x1, y1) that describes the location of the block on the page.
# Organized Data: The extracted data is organized into a list, where each item contains the page number, coordinates, and text content, making it straightforward to process or analyze further.
# Applications of Extracted Text Blocks
# Extracting text blocks with their coordinates can be particularly useful for:
#
# Content Analysis: Understanding the layout and structure of the document.
# Data Extraction: Extracting structured data from documents where the layout is significant (e.g., forms, reports).
# Search and Highlight: Locating and highlighting or annotating specific blocks that match certain criteria.
# Conclusion
# Using PyMuPDF to extract blocks from PDFs provides a powerful method for detailed text handling and positioning. If you need further customization, such as filtering blocks, extracting based on certain conditions, or more complex text analysis, let me know and I can guide you through more specific scenarios or help enhance the solution!

def pdf_extraction(path):
    # creating a pdf reader object
    pdf_reader = PdfReader(path)
    metadata = pdf_reader.metadata
    # Extracting creation and modification dates
    author = metadata.author
    title = metadata.title
    subject = metadata.subject
    creator = metadata.creator
    producer = metadata.producer
    creation_date = metadata.creation_date.strftime("%Y-%m-%d %H:%M:%S")
    modification_date = metadata.modification_date.strftime("%Y-%m-%d %H:%M:%S")

    number_of_pages = len(pdf_reader.pages)

    # one for each text run in presentation
    prefix = datetime.now().strftime("Y%Ym%md%d-H%HM%MS%S")
    extract_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    output_path = f"./pdf/scan/{prefix}/"
    path_exists = os.path.exists(output_path)
    if not path_exists:
        # Create a new directory because it does not exist
        os.makedirs(output_path)
    logging.basicConfig(filename=f'{output_path}conversion.log', encoding='utf-8', level=logging.INFO)
    logging.info(f"Processing the pdf document {path}")
    logger.info(f"number of pages={number_of_pages}")

    meta_data = {"file": path,
                 "page count": number_of_pages,
                 "author": pdf_reader.metadata.author,
                 "created on": f" {creation_date} UTC",
                 "modified on": f" {modification_date} UTC",
                 "extracted on": f" {extract_time} UTC"}
    with open(f"{output_path}/meta-data.json", 'w') as f:
        f.write(json.dumps(meta_data, indent=4))

    all_text_list = []
    for i, page in enumerate(pdf_reader.pages):
        output_path = f"{output_path}/page-{i + 1}"
        exists = os.path.exists(output_path)
        if not exists:
            # Create a new directory because it does not exist
            os.makedirs(output_path)
        # page = pdf_reader.pages[i]

        # extracting text from page
        text = page.extract_text()
        with open(f"{output_path}/page.txt", 'w') as f:
            f.writelines(text)
        count = 0
        all_text_list.append(text)
        for image_file_object in page.images:
            with open(f"{output_path}/{str(count) + image_file_object.name}", "wb") as fp:
                fp.write(image_file_object.data)
                count += 1

    document_text = json.dumps({'document_text': all_text_list}, indent=4)
    with open(f"{output_path}/joined.json", 'a', encoding="utf-8") as f:
        f.write(document_text)

    # dump_csv(all_text_list, f"{output_path}/joined.csv")
    print('Done')

def convert_pdf_to_png(pdf_path):
    """
    :param pdf_path: like "my_pdf_file.pdf"
    :return: None
    """
    pdf_object = pdfium.PdfDocument(pdf_path)
    n_pages = len(pdf_object)
    for page_number in range(n_pages):
        p = pdf_object.get_page(page_number)
        pil_image = p.render(scale=300 / 72).to_pil()
        # render(self, scale=1, rotation=0, crop=(0, 0, 0, 0),
        #      may_draw_forms=True,
        #      bitmap_maker=<bound method PdfBitmap.new_native of <class 'pypdfium2._helpers.bitmap.PdfBitmap'>>,
        #      color_scheme=None, fill_to_stroke=False, **kwargs)
        pil_image.save(f"image_{page_number+1}.png")


def convert_pdf_file_to_png(pdf_path):
    output_file = pdf_path + '.png'
    p = convert_from_path(pdf_path, dpi=200, fmt='png', output_file=output_file)
#
# def pdf_extraction(path_to_presentation):
#     prs = Presentation(path_to_presentation)
#     prs_shaper = ShapePresentation()
#     prs_shaper.LoadFromFile(path_to_presentation)
#     base_name = os.path.splitext(os.path.basename(path_to_presentation))[0]
#     # text_runs will be populated with a list of strings,
#     # one for each text run in presentation
#     prefix = datetime.now().strftime("Y%Ym%md%d-H%HM%MS%S")
#     extract_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#     output_path = f"./pptx/scan/{prefix}/"
#     path_exists = os.path.exists(output_path)
#     if not path_exists:
#         # Create a new directory because it does not exist
#         os.makedirs(output_path)
#     logging.basicConfig(filename=f'{output_path}conversion.log', encoding='utf-8', level=logging.INFO)
#     logging.info(f"Processing the power point file {path_to_presentation}")
#
#
#     all_text_list = []
#     for slide_number, slide in enumerate(prs.slides):
#         print(f"Processing slide {slide_number + 1} of {len(prs.slides)}")
#         # getting a specific page from the per file
#         output_path = f"./pptx/scan/{prefix}/slide-{slide_number + 1}"
#         path_exists = os.path.exists(output_path)
#         if not path_exists:
#             # Create a new directory because it does not exist
#             os.makedirs(output_path)
#         text_runs = []
#         for shape in slide.shapes:
#             t_runs, a_t_runs = process_shape(output_path, prs_shaper, slide_number, shape)
#             text_runs.extend(t_runs)
#             all_text_list.extend(a_t_runs)
#         # new text runs find connected shapes.json(text_runs)
#         # if new_text_runs:
#         #     print("Start Shape:", new text_runs name if new text runs [0] else "None")
#         #     print("End Shape:", new text runs [1] name if new text runs [1] else "None")
#         with open(f"{output_path}/text_runs.json", 'a', encoding="utf-8") as f:
#             f.write(json.dumps({'page text': text_runs}, indent=4))
#             # for t in text_runs:
#             #     f.write(f"{t['slide']}|{t['x']}|{t['y']){t['text']}\n")
#             #     all_text_list.append(t)
#             #     f.write(f*(bytes (t, 'utf-8').decode('unicode_escape')}\n*)
#         xml_string = convert_slide_json_to_connect_struct(f"{base_name} slide-{slide_number + 1}", text_runs)
#         with open(f"{output_path}/slide_arch.xml", 'a', encoding="utf-8") as f:
#             f.write(xml_string)
#
#     output_path = f"./pptx/scan/{prefix}"
#     path_exists = os.path.exists(output_path)
#     if not path_exists:
#         # Create a new directory because it does not exist
#         os.makedirs(output_path)
#     # Zero Width String
#     # joined = '\n'.join(json.dumps (all_text_list))
#     slide_text = json.dumps({'deck_text': all_text_list}, indent=4)
#     with open(f"{output_path}/joined.json", 'a', encoding="utf-8") as f:
#         f.write(slide_text)
#
#     dump_csv(all_text_list, f"{output_path}/joined.csv")
#



if __name__ == "__main__":
    """
    Convert a PDF file to a PNG, page by page then extract the text and graphics and into json files
    """
    # convert_pdf_to_png('./incoming/ems-color-system-diagram.pdf')
    logger.setLevel(logging.DEBUG)
    run_directory = os.getcwd()
    DOWNLOAD_PATH = str(Path.home() / "Downloads")
    INCOMING_PATH = "./incoming"
    pdf_path =f"{INCOMING_PATH}/TESTLAYOUT.pdf"
    # pdf_path =f"{INCOMING_PATH}/0028504.pdf"
    # pdf_path =f"{INCOMING_PATH}/GridSpice A Distributed Simulation Platform for the Smart Grid.pdf"

    print(f"Processing '{pdf_path}'")
    pdf_extraction2(pdf_path)

