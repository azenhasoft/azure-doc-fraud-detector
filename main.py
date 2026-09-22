"""Exemplo de extração de dados com Azure Document Intelligence."""

import argparse
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

API_VERSION = "2023-10-31"
TIMEOUT = 30
INTERVALO = 2
TENTATIVAS = 30


def analisar_documento(caminho: Path, endpoint: str, chave: str) -> dict:
    url = (
        f"{endpoint.rstrip('/')}/formrecognizer/documentModels/"
        f"prebuilt-document:analyze?api-version={API_VERSION}"
    )
    headers = {
        "Content-Type": "application/pdf",
        "Ocp-Apim-Subscription-Key": chave,
    }

    with caminho.open("rb") as arquivo:
        resposta = requests.post(url, headers=headers, data=arquivo, timeout=TIMEOUT)
    resposta.raise_for_status()
    if resposta.status_code != 202 or "operation-location" not in resposta.headers:
        raise RuntimeError("O Azure não retornou o endereço da operação.")

    url_resultado = resposta.headers["operation-location"]
    for _ in range(TENTATIVAS):
        resposta = requests.get(
            url_resultado,
            headers={"Ocp-Apim-Subscription-Key": chave},
            timeout=TIMEOUT,
        )
        resposta.raise_for_status()
        resultado = resposta.json()
        estado = resultado.get("status")

        if estado == "succeeded":
            return resultado
        if estado in {"failed", "canceled"}:
            raise RuntimeError(f"Análise encerrada com status: {estado}")
        time.sleep(INTERVALO)

    raise TimeoutError("A análise não terminou no tempo esperado.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrai dados de um PDF com Azure.")
    parser.add_argument("documento", type=Path, help="Caminho do arquivo PDF")
    args = parser.parse_args()

    load_dotenv()
    endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
    chave = os.getenv("FORM_RECOGNIZER_KEY")
    if not endpoint or not chave:
        parser.error("Defina FORM_RECOGNIZER_ENDPOINT e FORM_RECOGNIZER_KEY.")
    if not args.documento.is_file() or args.documento.suffix.lower() != ".pdf":
        parser.error("Informe um arquivo PDF existente.")

    try:
        resultado = analisar_documento(args.documento, endpoint, chave)
    except (requests.RequestException, RuntimeError, TimeoutError) as erro:
        parser.exit(1, f"Falha na análise: {erro}\n")

    for pagina in resultado.get("analyzeResult", {}).get("pages", []):
        for linha in pagina.get("lines", []):
            print(linha.get("content", ""))


if __name__ == "__main__":
    main()
