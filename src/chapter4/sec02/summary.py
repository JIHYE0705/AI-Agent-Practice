from pathlib import Path

from src.ai_clients.ollama_client import OllamaClient


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


if __name__ == '__main__':
    project_path = Path(__file__).resolve().parent.parent
    file_path = f'{project_path}/output/LLM_with_preprocessing.txt'

    summary = summarise_txt(file_path)
    print(summary)

    txt_file_name = f'{project_path}/output/crop_model_summary.txt'

    with open(txt_file_name, 'w', encoding='utf-8') as f:
        f.write(summary)
