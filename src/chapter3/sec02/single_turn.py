from src.ai_clients.ollama_client import OllamaClient

ollama = OllamaClient()
if __name__ == '__main__':
    while True:
        user_input = input('사용자: ')

        if user_input == 'exit':
            break

        response = ollama.chat(
            messages=[
                {
                    'role': 'system', 'content': '너는 사용자를 도와주는 상담사야'
                },
                {
                    'role': 'user', 'content': user_input
                }
            ]
        )
        print('AI: ' + response['message']['content'])
