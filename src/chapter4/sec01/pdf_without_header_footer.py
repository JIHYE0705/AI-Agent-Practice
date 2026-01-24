import os
from pathlib import Path

import pymupdf

if __name__ == '__main__':
    file_path = Path(__file__).resolve().parent.parent
    pdf_file_name = f'{file_path}/data/LLM.pdf'

    doc = pymupdf.open(pdf_file_name)

    header_height = 80
    footer_height = 80

    full_text = ''

    for page in doc:
        rect = page.rect  # 페이지 크기 가져오기

        header = page.get_text(clip=(0, 0, rect.width, header_height))
        footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height))
        text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))

        full_text += text + '\n----------------------------------------\n'

    pdf_file_name = os.path.basename(pdf_file_name)
    pdf_file_name = os.path.splitext(pdf_file_name)[0]  # 확장자 제거

    txt_file_name = f'{file_path}/output/{pdf_file_name}_with_preprocessing.txt'

    with open(txt_file_name, 'w', encoding='utf-8') as f:
        f.write(full_text)
