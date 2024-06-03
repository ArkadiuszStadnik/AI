import requests

def ask_ollama_for_rag(pytanie, tekst):
    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "llama3",
        "prompt": "Odpowiedz na pytanie: " + pytanie + "w oparciu tekst. Tekst: " + tekst,
        "stream": False,
    }

    return get_response(data, url)

def ask_ollama_for_rag(pytanie, tekst, config):
    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "llama3",
        "prompt": "Odpowiedz na pytanie: " + pytanie + "w oparciu tekst. Tekst: " + tekst,
        "stream": False,
        "options": {
            "temperature": config["temperature"],
            "top_p": config["top_p"],
            "num_predict": config["max_length"]
        }
    }
    return get_response(data, url)

def ask_ollama(pytanie):
    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "llama3",
        "prompt": "Odpowiedz na pytanie: " + pytanie ,
        "stream": False
    }

    return get_response(data, url)

def get_response(data, url):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Sukces!")
        print("Odpowiedź serwera:")
        print(response.json()["response"])
        print("********printuje body******")
    else:
        print("Błąd! Kod statusu:", response.status_code)
    return response.json()["response"]