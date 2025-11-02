import requests
import os
import time
from dotenv import load_dotenv

# carrega as variáveis do .env
load_dotenv()

# pega as credenciais do Azure
FORM_RECOGNIZER_ENDPOINT = os.getenv("FORM_RECOGNIZER_ENDPOINT")
FORM_RECOGNIZER_KEY = os.getenv("FORM_RECOGNIZER_KEY")

# caminho do documento que vamos analisar
documento = "assets/exemplo-documento.pdf"

# função que envia o documento pro Azure Form Recognizer
def analisar_documento(caminho_arquivo):
    url = f"{FORM_RECOGNIZER_ENDPOINT}/formrecognizer/documentModels/prebuilt-document:analyze?api-version=2023-10-31"
    headers = {
        "Content-Type": "application/pdf",
        "Ocp-Apim-Subscription-Key": FORM_RECOGNIZER_KEY
    }

    with open(caminho_arquivo, "rb") as f:
        documento = f.read()

    response = requests.post(url, headers=headers, data=documento)
    if response.status_code == 202:
        return response.headers["operation-location"]
    else:
        print("Erro ao enviar documento:", response.text)
        return None

# função que busca o resultado da análise
def buscar_resultado(url_resultado):
    headers = {
        "Ocp-Apim-Subscription-Key": FORM_RECOGNIZER_KEY
    }
    response = requests.get(url_resultado, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar resultado:", response.text)
        return None

# executa o fluxo
print("Enviando documento para análise...")
url_resultado = analisar_documento(documento)

if url_resultado:
    print("Análise iniciada. Aguardando resultado...")
    time.sleep(10)  # espera um pouco antes de buscar

    resultado = buscar_resultado(url_resultado)

    if resultado:
        print("Resultado da análise:")
        for doc in resultado.get("analyzeResult", {}).get("documents", []):
            print(doc)
    else:
        print("Não foi possível obter o resultado.")
else:
    print("Falha ao iniciar análise.")
