from ollama_client import OllamaClient

ollama = OllamaClient()


def get_ai_response(messages):
    response = ollama.chat(messages=messages)
    return response['message']['content']


if __name__ == '__main__':
    messages = [
        {'role': 'system', 'content': '너는 사용자를 도와주는 상담사야'}
    ]

    while True:
        user_input = input('사용자: ')

        if user_input == 'exit':
            break

        messages.append({'role': 'user', 'content': user_input})
        ai_response = get_ai_response(messages)

        messages.append({'role': 'assistant', 'content': ai_response})

        print('AI: ' + ai_response)
