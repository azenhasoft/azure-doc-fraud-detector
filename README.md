# Azure Document Analysis

Este projeto começou com uma ideia bem maior: estudar como Azure e Python poderiam ser usados em um fluxo de validação de documentos e, mais adiante, experimentar formas de detectar possíveis fraudes.

O código ainda está no começo desse caminho.

Hoje ele faz uma coisa específica: envia um PDF para o Azure Document Intelligence e consulta o resultado da análise. Ainda não existe detecção de fraude no projeto.

Prefiro deixar isso claro aqui do que apresentar como pronto algo que ainda quero construir.

## O que funciona hoje

O fluxo atual está em `main.py`:

1. o programa lê o endpoint e a chave do Azure pelo arquivo `.env`;
2. abre um PDF local;
3. envia o arquivo para o modelo `prebuilt-document`;
4. recebe o endereço da operação criada pelo Azure;
5. espera alguns segundos;
6. consulta o resultado e mostra a resposta no terminal.

Em resumo:

```text
PDF
 ↓
Python
 ↓
Azure Document Intelligence
 ↓
Extração do documento
 ↓
Resultado no terminal
```

É um proof of concept, não uma aplicação pronta para produção.

## Como testar

Você precisa de Python 3.10 ou superior e de um recurso do Azure Document Intelligence com endpoint e chave válidos.

Clone o projeto e crie o ambiente virtual:

```bash
git clone https://github.com/azenhasoft/azure-doc-fraud-detector.git
cd azure-doc-fraud-detector

python -m venv .venv
```

Depois de ativar o ambiente:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` local seguindo o modelo de `.env.example`:

```text
FORM_RECOGNIZER_ENDPOINT=https://seu-recurso.cognitiveservices.azure.com
FORM_RECOGNIZER_KEY=sua-chave
```

O `.env` não deve ser enviado para o GitHub.

Para executar:

```bash
python main.py
```

No estado atual, o script procura o documento neste caminho:

```text
assets/exemplo-documento.pdf
```

O repositório não inclui esse PDF. Para testar, é preciso criar a pasta `assets` e colocar nela um documento próprio com esse nome.

## O que ainda não existe

A ideia original do projeto envolvia muito mais coisas do que o código atual implementa.

Por enquanto, **não há**:

- classificação de documentos como fraudulentos ou legítimos;
- análise de assinatura ou adulteração de imagem;
- Azure Computer Vision;
- integração com OpenAI ou outro LLM;
- FastAPI;
- dashboard;
- banco de dados;
- score de fraude;
- métricas de acurácia;
- Key Vault ou Application Insights.

Também não tenho dados que sustentem números de acurácia, desempenho, custo por documento ou volume processado. Quando houver algo desse tipo, quero que venha de teste e medição, não de estimativa colocada no README.

## Limitações do código atual

Há bastante espaço para melhorar o próprio protótipo.

O caminho do PDF ainda está escrito diretamente no código. O programa também espera dez segundos antes de consultar o Azure, em vez de acompanhar o status da operação até ela terminar.

Ainda faltam validações para configuração e arquivo, tratamento melhor de erros de rede e testes automatizados.

Tudo isso vem antes de transformar o projeto em algo maior.

## Onde quero chegar

Minha ideia é evoluir por partes:

- [ ] receber o caminho do documento pela linha de comando
- [ ] validar arquivo e configuração antes do envio
- [ ] acompanhar corretamente o status da operação no Azure
- [ ] melhorar mensagens e tratamento de erros
- [ ] criar testes para as partes que não dependem diretamente da API
- [ ] adicionar um documento fictício para demonstração
- [ ] organizar melhor os dados retornados pelo Azure
- [ ] experimentar regras simples de validação documental
- [ ] estudar uma abordagem real para detecção de fraude

A última etapa é justamente a mais difícil.

Extrair informações de um documento e detectar fraude são problemas diferentes. Para chamar este projeto de detector de fraude, eu precisaria ter dados adequados, critérios de avaliação e resultados que mostrassem que a detecção realmente funciona.

Ainda não cheguei lá.

## Sobre segurança

As credenciais do Azure ficam em variáveis de ambiente e o arquivo `.env` está no `.gitignore`.

Se uma chave real for publicada por engano em algum momento, apenas apagar o arquivo do repositório não resolve o problema, porque ela pode continuar no histórico do Git. Nesse caso, a chave precisa ser revogada e substituída no Azure.

## Por que mantenho este projeto

Porque ele mostra uma parte do aprendizado que ainda está acontecendo.

A primeira versão da ideia era ambiciosa demais para o código que eu tinha. Em vez de apagar o projeto ou fingir que tudo aquilo já estava implementado, preferi voltar ao que realmente funciona e continuar dali.

Se um dia este repositório se tornar de fato um detector de fraude, quero conseguir olhar o histórico e ver como cheguei até lá.
