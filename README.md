# Azure Document Analysis — Proof of Concept

Proof of concept em Python para enviar um documento PDF ao **Azure Document Intelligence** (endpoint historicamente conhecido como Form Recognizer) e consultar o resultado da análise.

Este repositório explora uma etapa que pode fazer parte de um fluxo futuro de validação documental. **No estado atual, ele não detecta fraude, não classifica documentos como legítimos ou fraudulentos e não deve ser usado para decisões reais de segurança ou conformidade.**

## Estado atual

O código implementado em `main.py`:

1. carrega o endpoint e a chave do Azure por variáveis de ambiente;
2. lê um PDF local;
3. envia o documento ao modelo `prebuilt-document`;
4. recebe a URL da operação assíncrona;
5. aguarda antes de consultar o resultado;
6. imprime os documentos retornados pela API.

Fluxo atual:

```text
PDF local
   ↓
Python / requests
   ↓
Azure Document Intelligence
   ↓
Resultado da extração
   ↓
Saída no terminal
```

## O que este projeto ainda NÃO implementa

Para evitar confundir protótipo com produto pronto, estes recursos não fazem parte do código atual:

- detecção ou classificação de fraude;
- análise de assinatura;
- Azure Computer Vision;
- OpenAI ou outro LLM;
- FastAPI ou API REST própria;
- dashboard;
- banco de dados ou audit log;
- Azure Key Vault;
- Application Insights;
- score de fraude ou métricas de acurácia;
- garantias de LGPD, ISO 27001 ou OWASP;
- métricas de produção, SLA, throughput ou custo por documento.

Esses itens só devem ser descritos como implementados quando houver código, configuração e evidências correspondentes no repositório.

## Requisitos

- Python 3.10+
- uma conta Azure com um recurso compatível de Document Intelligence
- endpoint e chave de acesso válidos

Instale as dependências:

```bash
git clone https://github.com/azenhasoft/azure-doc-fraud-detector.git
cd azure-doc-fraud-detector

python -m venv .venv
```

Ative o ambiente virtual e execute:

```bash
pip install -r requirements.txt
```

Crie seu arquivo `.env` local a partir do exemplo:

```text
FORM_RECOGNIZER_ENDPOINT=https://seu-recurso.cognitiveservices.azure.com
FORM_RECOGNIZER_KEY=sua-chave
```

> Nunca faça commit de chaves reais. O arquivo `.env` está listado no `.gitignore`.

## Executando

O script atualmente espera um PDF no caminho:

```text
assets/exemplo-documento.pdf
```

Depois:

```bash
python main.py
```

Como o repositório ainda não inclui um documento de exemplo, você precisa criar a pasta `assets` e fornecer um PDF próprio para realizar o teste.

## Limitações técnicas atuais

O projeto ainda é um experimento pequeno e possui limitações deliberadamente documentadas:

- o caminho do PDF está fixo no código;
- o `Content-Type` está fixo como `application/pdf`;
- a consulta da operação usa uma espera fixa de 10 segundos em vez de polling robusto;
- não há validação explícita das variáveis de ambiente;
- não há tratamento estruturado de exceções de rede;
- não há testes automatizados;
- não há CLI com argumentos;
- o resultado é apenas impresso no terminal.

## Roadmap

A evolução do projeto pode ser feita em etapas verificáveis:

- [ ] aceitar o caminho do documento por argumento de linha de comando;
- [ ] validar configuração e arquivo antes do envio;
- [ ] substituir a espera fixa por polling do status da operação;
- [ ] melhorar tratamento de erros e timeouts;
- [ ] criar testes para a lógica que puder ser isolada da API;
- [ ] adicionar um PDF sintético de demonstração sem dados pessoais;
- [ ] estruturar a saída extraída em um formato próprio;
- [ ] experimentar regras de validação documental;
- [ ] somente depois, pesquisar e prototipar sinais de fraude com datasets e métricas apropriados.

Uma futura solução de detecção de fraude exigiria dados rotulados, critérios de avaliação, testes e validação muito além da simples extração de documentos.

## Segurança

Credenciais devem existir apenas no ambiente local ou em um serviço apropriado de gerenciamento de segredos. Caso uma chave tenha sido publicada anteriormente em um commit, removê-la do arquivo atual **não invalida a credencial**: ela deve ser revogada/rotacionada no provedor.

## Objetivo do repositório

Este projeto é mantido como registro de aprendizado e como ponto de partida para explorar processamento documental com Python e Azure.

A intenção do roadmap é evoluir o protótipo por meio de implementações demonstráveis, mantendo a documentação alinhada ao código.
