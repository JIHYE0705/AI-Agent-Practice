import os.path
from pathlib import Path

import pymupdf

if __name__ == '__main__':
    file_path = Path(__file__).resolve().parent
    pdf_file_name = f'{file_path}/data/LLM.pdf'

    doc = pymupdf.open(pdf_file_name)

    full_text = ''

    for page in doc:
        text = page.get_text()
        full_text += text

    pdf_file_name = os.path.basename(pdf_file_name)
    pdf_file_name = os.path.splitext(pdf_file_name)[0]

    txt_file_name = f'{file_path}/output/{pdf_file_name}.txt'
    with open(txt_file_name, 'w', encoding='utf-8') as f:
        f.write(full_text)