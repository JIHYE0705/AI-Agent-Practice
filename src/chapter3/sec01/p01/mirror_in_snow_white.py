from src.ai_clients.ollama_client import OllamaClient

ollama = OllamaClient()

if __name__ == '__main__':
    messages = [
        {
            'role': 'system',
            'content': '너는 백설공주 이야기 속의 마법 거울이야. 그 이야기의 캐릭터에 부합하게 답변해줘'
        },
        {
            'role': 'user', 'content': '세상에서 누가 제일 아름답니?'
        }
    ]
    response = ollama.chat(messages=messages)
    print(response)
