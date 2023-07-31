# 💬 Chatgpt Python bot
Script básico de Python que se conecta con la API de gpt-3.5 de OpenAI.

# Requerimientos
* Python 3.7.1
* openai 0.27.0
* python-dotenv 0.21.1

# Configuración
## Configura tu archvio env
1. Copia el archivo .eng-template y renómbralo .env

## Consigue tu API key de OpenAI
1. Créate una cuenta en OpenAI
2. En el menú lateral anda a User > API Keys (https://platform.openai.com/account/api-keys)
3. Haz click en Create new secret key
4. Copia tu API key secreta y pégala en la variable OPENAI_API_KEY en el archivo .env

## Ejecuta el script de Python
```sh
python3 main.py
```