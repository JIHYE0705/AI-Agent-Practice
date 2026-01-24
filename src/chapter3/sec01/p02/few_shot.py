from src.ai_clients.ollama_client import OllamaClient

ollama = OllamaClient()

if __name__ == '__main__':
    messages = [
        {"role": "system", "content": "너는 유치원생이다. 동물이 나오면 울음소리로 답해라."},
        {"role": "user", "content": "참새"},
        {"role": "assistant", "content": "짹짹"},
        {"role": "user", "content": "말"},
        {"role": "assistant", "content": "히이잉"},
        {"role": "user", "content": "개구리"},
        {"role": "assistant", "content": "개굴개굴"},
        {"role": "user", "content": "닭"},
    ]
    response = ollama.chat(messages=messages)
    print(response['message']['content'])
