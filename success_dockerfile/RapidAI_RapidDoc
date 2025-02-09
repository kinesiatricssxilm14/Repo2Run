FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/RapidAI/RapidDoc.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /RapidDoc/. /repo && rm -rf /RapidDoc/ && \
    rm -rf /RapidDoc && \
    cd /repo && git checkout 5e5fef5e7d02bb646111e063e041566318596c50 && \
    pip install filetype==1.2.0 && \
    pip install rapid-layout==0.4.0 && \
    pip install numpy==1.26.4 && \
    pip install opencv_python_headless==4.10.0.84 && \
    pip install pdfminer.six==20231228 && \
    pip install Pillow==11.0.0 && \
    pip install tqdm==4.67.1 && \
    pip install pymupdf==1.25.1 && \
    pip install camelot-py==0.11.0 && \
    pip install pdf2image==1.17.0 && \
    pip install pdfplumber==0.11.4 && \
    pip install shapely==2.0.6 && \
    apt-get update -qq && \
    apt-get install -y -qq poppler-utils && \
    pip install rapidocr-onnxruntime==1.4.3 && \
    echo "1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 24 Tf 36 700 Td (Hello, PDF world!) Tj ET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF" > /repo/1.pdf && \
    mkdir -p /repo/path/to && \
    cd /repo && echo "1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 24 Tf 36 700 Td (Hello, PDF world!) Tj ET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF" > 1.pdf && \
    cd /repo && mkdir -p /repo/path/to && \
    cd /repo && mkdir -p /repo/path/to && \
    cd /repo && echo "1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj 2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj 3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >> endobj 4 0 obj << /Length 44 >> stream BT /F1 24 Tf 36 700 Td (Hello, PDF world!) Tj ET endstream endobj 5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj trailer << /Root 1 0 R >> %%EOF" > 1.pdf && \
    pip install PyPDF2==3.0.1 && \
    echo "from PyPDF2 import PdfFileWriter; file_writer = PdfFileWriter(); file_writer.addBlankPage(width=612, height=792); with open('/repo/1.pdf', 'wb') as f: file_writer.write(f)" > /repo/create_pdf.py && \
    echo "from PyPDF2 import PdfFileWriter; file_writer = PdfFileWriter(); file_writer.addBlankPage(width=612, height=792); output = open('/repo/1.pdf', 'wb'); file_writer.write(output); output.close()" > /repo/create_pdf.py && \
    echo "from PyPDF2 import PdfWriter; file_writer = PdfWriter(); file_writer.addBlankPage(width=612, height=792); output = open('/repo/1.pdf', 'wb'); file_writer.write(output); output.close()" > /repo/create_pdf.py && \
    echo "from PyPDF2 import PdfWriter; file_writer = PdfWriter(); file_writer.add_blank_page(width=612, height=792); output = open('/repo/1.pdf', 'wb'); file_writer.write(output); output.close()" > /repo/create_pdf.py && \
    python3 /repo/create_pdf.py && \
    mkdir -p /repo/path/to && \
    cp /repo/1.pdf /repo/path/to/pdf && \
    echo "from pathlib import Path; from rapid_doc.pdf_extract.main import PDFExtract; pdf_path = Path('tests/test_files/direct_extract/single_column.pdf'); extract = PDFExtract(); extract.extract_all_pages(pdf_path);" > /repo/setup_pdf_extract.py && \
    mkdir -p /repo/tests/test_files/direct_extract/ && \
    python3 -c "from PyPDF2 import PdfWriter; file_writer = PdfWriter(); file_writer.add_blank_page(width=612, height=792); output = open('/repo/tests/test_files/direct_extract/single_column.pdf', 'wb'); file_writer.write(output); output.close()" && \
    echo "from pathlib import Path; from rapid_doc.pdf_extract.main import PDFExtract; pdf_path = Path('/repo/tests/test_files/direct_extract/single_column.pdf'); extract = PDFExtract(); extract.extract_all_pages(pdf_path);" > /repo/setup_pdf_extract.py && \
    python3 /repo/setup_pdf_extract.py && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    mkdir -p /path/to && \
    ln -s /repo/1.pdf /path/to/pdf && \
    echo "from pathlib import Path; from rapid_doc.pdf_extract.main import PDFExtract; pdf_path = Path('/repo/tests/test_files/direct_extract/single_column.pdf'); extract = PDFExtract(pdf_path); pdf_img_list = extract.read_pdf(pdf_path); pdf_nums = extract.get_page_count(pdf_path); print('ok')" > /repo/helper_test_pdf_extract.py && \
    python3 /repo/helper_test_pdf_extract.py && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch" && \
    python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch" && \
    python /code_edit.py -t "/search_patch/14.patch" && \
    python /code_edit.py -t "/search_patch/15.patch" && \
    python /code_edit.py -t "/search_patch/16.patch" && \
    python /code_edit.py -t "/search_patch/17.patch" && \
    python /code_edit.py -t "/search_patch/18.patch" && \
    python /code_edit.py -t "/search_patch/19.patch" && \
    python /code_edit.py -t "/search_patch/20.patch" && \
    python /code_edit.py -t "/search_patch/21.patch" && \
    python /code_edit.py -t "/search_patch/22.patch" && \
    python /code_edit.py -t "/search_patch/23.patch" && \
    python /code_edit.py -t "/search_patch/24.patch" && \
    python /code_edit.py -t "/search_patch/25.patch" && \
    python /code_edit.py -t "/search_patch/26.patch" && \
    python /code_edit.py -t "/search_patch/27.patch" && \
    python /code_edit.py -t "/search_patch/28.patch" && \
    python /code_edit.py -t "/search_patch/29.patch" && \
    python /code_edit.py -t "/search_patch/30.patch" && \
    python /code_edit.py -t "/search_patch/31.patch" && \
    python /code_edit.py -t "/search_patch/32.patch" && \
    python /code_edit.py -t "/search_patch/33.patch" && \
    python /code_edit.py -t "/search_patch/34.patch" && \
    python /code_edit.py -t "/search_patch/35.patch" && \
    python /code_edit.py -t "/search_patch/36.patch" && \
    python /code_edit.py -t "/search_patch/37.patch" && \
    python /code_edit.py -t "/search_patch/38.patch" && \
    python /code_edit.py -t "/search_patch/39.patch" && \
    python /code_edit.py -t "/search_patch/40.patch" && \
    python /code_edit.py -t "/search_patch/41.patch" && \
    python /code_edit.py -t "/search_patch/42.patch" && \
    python /code_edit.py -t "/search_patch/43.patch" && \
    python /code_edit.py -t "/search_patch/44.patch" && \
    python /code_edit.py -t "/search_patch/45.patch" && \
    python /code_edit.py -t "/search_patch/46.patch" && \
    python /code_edit.py -t "/search_patch/47.patch" && \
    python /code_edit.py -t "/search_patch/48.patch" && \
    python /code_edit.py -t "/search_patch/49.patch" && \
    python /code_edit.py -t "/search_patch/50.patch" && \
    python /code_edit.py -t "/search_patch/51.patch" && \
    python /code_edit.py -t "/search_patch/52.patch" && \
    python /code_edit.py -t "/search_patch/53.patch" && \
    python /code_edit.py -t "/search_patch/54.patch" && \
    python /code_edit.py -t "/search_patch/55.patch" && \
    python /code_edit.py -t "/search_patch/56.patch" && \
    python /code_edit.py -t "/search_patch/57.patch" && \
    python /code_edit.py -t "/search_patch/58.patch" && \
    python /code_edit.py -t "/search_patch/59.patch" && \
    python /code_edit.py -t "/search_patch/60.patch" && \
    python /code_edit.py -t "/search_patch/61.patch" && \
    python /code_edit.py -t "/search_patch/62.patch" && \
    python /code_edit.py -t "/search_patch/63.patch" && \
    python /code_edit.py -t "/search_patch/64.patch" && \
    python /code_edit.py -t "/search_patch/65.patch" && \
    python /code_edit.py -t "/search_patch/66.patch" && \
    python /code_edit.py -t "/search_patch/67.patch" && \
    python /code_edit.py -t "/search_patch/68.patch" && \
    python /code_edit.py -t "/search_patch/69.patch" && \
    python /code_edit.py -t "/search_patch/70.patch" && \
    python /code_edit.py -t "/search_patch/71.patch" && \
    python /code_edit.py -t "/search_patch/72.patch" && \
    python /code_edit.py -t "/search_patch/73.patch" && \
    python /code_edit.py -t "/search_patch/74.patch" && \
    python /code_edit.py -t "/search_patch/75.patch" && \
    python /code_edit.py -t "/search_patch/76.patch" && \
    python /code_edit.py -t "/search_patch/77.patch" && \
    python /code_edit.py -t "/search_patch/78.patch" && \
    python /code_edit.py -t "/search_patch/79.patch" && \
    python /code_edit.py -t "/search_patch/80.patch" && \
    python /code_edit.py -t "/search_patch/81.patch" && \
    python /code_edit.py -t "/search_patch/82.patch" && \
    python /code_edit.py -t "/search_patch/83.patch"