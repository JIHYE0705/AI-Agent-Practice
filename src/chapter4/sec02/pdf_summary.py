import os
from pathlib import Path

import pymupdf

from src.ai_clients.ollama_client import OllamaClient

root_path = Path(__file__).resolve().parent.parent


def pdf_to_text(pdf_file_path):
    doc = pymupdf.open(pdf_file_path)

    header_height = 80
    footer_height = 80

    full_text = ''

    for page in doc:
        rect = page.rect

        header = page.get_text(clip=(0, 0, rect.width, header_height))
        footer = page.get_text(clip=(0, rect.height - footer_height, rect.width, rect.height))
        text = page.get_text(clip=(0, header_height, rect.width, rect.height - footer_height))

        full_text += text + '\n--------------------------------\n'

    pdf_file_name = os.path.basename(pdf_file_path)
    pdf_file_name = os.path.splitext(pdf_file_name)[0]

    txt_file_path = f'{root_path}/output/{pdf_file_name}_with_preprocessing.txt'

    with open(txt_file_path, 'w', encoding='utf-8') as f:
        f.write(full_text)

    return txt_file_path


def summarise_txt(file_path: str):
    ollama = OllamaClient()

    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 저자의 문제 인식과 주장을 파악하고, 주요 내용을 요약하라.

    작성해야 하는 포맷은 다음과 같다.

    # 제목

    ## 저자의 문제 인식 및 주장 (15문장 이내)

    ## 저자 소개

    ================= 이하 텍스트 =================

    {txt} 
'''

    print(system_prompt)
    print('===================================================')

    response = ollama.chat(messages=[{'role': 'system', 'content': system_prompt}])

    return response['message']['content']


def summarize_pdf(pdf_file_path, output_file_path):
    txt_file_path = pdf_to_text(pdf_file_path)
    summary = summarise_txt(txt_file_path)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(summary)


if __name__ == '__main__':
    pdf_file_path = f'{root_path}/data/LLM.pdf'
    summarize_pdf(pdf_file_path, f'{root_path}/output/crop_model_summary2.txt')