from typing import Optional, List, Dict
import requests


class OllamaClient:
    def __init__(self, model: str = "qwen2.5:7b", timeout: int = 120, temperature: float = 0.1, ):
        self.base_url = "http://localhost:11434"
        self.model = model
        self.timeout = timeout
        self.temperature = temperature

    def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None, ) -> str:
        payload = {
            "model": model or self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": self.temperature
            }
        }

        res = requests.post(
            f"{self.base_url}/api/chat",
            json=payload,
            timeout=self.timeout
        )
        res.raise_for_status()

        return res.json()
