# chatbot-openrouter

Chatbot en Python usando la API de OpenRouter.

## Estructura

```
openrouterchat/
├── .venv/            # entorno virtual (no se sube a git)
├── .env              # tu API key (no se sube a git)
├── .gitignore
├── main.py           # el chatbot
├── requirements.txt
└── README.md
```

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Crea un archivo `.env` en la carpeta del proyecto con tu clave de OpenRouter:

```
OPENROUTER_API_KEY=tu_clave
```

Luego ejecuta:

```powershell
python main.py
```

Escribe `salir` para terminar el chat.
