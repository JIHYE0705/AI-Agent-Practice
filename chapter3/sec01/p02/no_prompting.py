from ollama_client import OllamaClient

ollama = OllamaClient()

if __name__ == '__main__':
    messages = [
        {

            'role': 'system', 'content': '너는 유치원생이야. 유치원생처럼 답변해줘'
        },
        {
            'role': 'user', 'content': '오리'
        }
    ]
    response = ollama.chat(messages=messages)
    print(response)
