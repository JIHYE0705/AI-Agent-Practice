from ollama_client import OllamaClient

ollama = OllamaClient()

if __name__ == '__main__':
    messages = [
        {"role": "system", "content": "너는 유치원생이다. 동물이 나오면 울음소리로 답해라."},
        {"role": "user", "content": "참새"},
        {"role": "assistant", "content": "짹짹"},
        {"role": "user", "content": "오리"}
    ]
    response = ollama.chat(messages=messages)
    print(response)
