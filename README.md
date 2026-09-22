# Extração de dados de PDF com Azure Document Intelligence

Exemplo em Python que envia um PDF ao modelo `prebuilt-document` do Azure Document Intelligence e imprime as linhas de texto retornadas. O código faz uma chamada assíncrona à API e consulta o resultado até a análise terminar.

Este repositório **não implementa detecção de fraude**, classificação de documentos legítimos, API web ou métricas de precisão. O resultado da extração exige interpretação e revisão humana antes de qualquer decisão sobre autenticidade.

## Requisitos

- Python 3.10 ou superior e uma instância do Azure Document Intelligence.
- Um PDF local e a URL e chave da instância Azure.

## Executar

```bash
git clone https://github.com/azenhasoft/azure-doc-fraud-detector.git
cd azure-doc-fraud-detector
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cp .env.example .env
# Preencha .env com valores novos da sua instância.
python main.py caminho/para/documento.pdf
```

No Windows, copie `.env.example` para `.env` manualmente ou use `Copy-Item .env.example .env`. O arquivo `.env` é ignorado pelo Git. Nunca publique chaves reais no repositório.

O script aceita PDF, espera até 60 segundos pela conclusão (30 consultas com intervalo de 2 segundos, além do tempo das requisições) e mostra as linhas reconhecidas. Erros da API ou tempo esgotado encerram a execução com uma mensagem. O uso da API pode gerar custos na sua conta Azure.

## Arquivos

- `main.py`: envio do PDF e consulta do resultado.
- `requirements.txt`: dependências Python.
- `.env.example`: nomes das variáveis necessárias, sem credenciais.

Se alguma chave já foi publicada neste repositório, substitua-a no portal Azure. Remover o arquivo de uma branch não remove seu conteúdo do histórico de commits.
