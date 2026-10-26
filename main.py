import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

mensajes = [
    {"role": "system", "content": "Responde en español de forma clara."}
]

print("Chat iniciado. Escribe 'salir' para terminar.")

while True:
    texto = input("\nTú: ").strip()

    if texto.lower() == "salir":
        break

    if not texto:
        continue

    mensajes.append({"role": "user", "content": texto})

    try:
        respuesta = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "openrouter/free",
                "messages": mensajes
            },
            timeout=60
        )

        if respuesta.status_code != 200:
            print("Error de OpenRouter:", respuesta.status_code)
            mensajes.pop()
            continue

        contenido = respuesta.json()["choices"][0]["message"]["content"]
        print("\nIA:", contenido)
        mensajes.append({"role": "assistant", "content": contenido})

    except (requests.RequestException, ValueError, KeyError, IndexError):
        print("No se pudo obtener la respuesta. Intenta nuevamente.")
        mensajes.pop()