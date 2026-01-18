import json

from ollama_client import OllamaClient

ollama = OllamaClient()

if __name__ == '__main__':
    messages = [
        {
            'role': 'system',
            'content': '너는 베트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변해줘'
        },
        {
            'role': 'user', 'content': '세상에서 누가 제일 아름답니?'
        }
    ]
    response = ollama.chat(messages=messages)
    print(response)
