# Desafio para Vaga de Engenheiro de IA

## Descrição

Crie um servidor em Python com um endpoint que recebe uma pergunta e classifica a pergunta em diferentes tipos. O endpoint deve ser capaz de identificar o tipo da pergunta com base no seguinte critério:

- **VEHICLE_COMPATIBILITY**: dúvida de compatibilidade com veículo.
- **PRODUCT_SPECIFICATION**: dúvida sobre a ficha técnica de um produto.
- **SEARCH_PRODUCT**: busca por outro produto.
- **PRICING**: dúvida sobre precificação.
- **UNDEFINED**: caso a pergunta não se encaixe em nenhum dos tipos acima.

### Requisitos

1. O servidor deve aceitar uma requisição **POST** no endpoint **`/chatbot`**.
2. O corpo da requisição deve conter um JSON com a chave **`question`**, que é a pergunta do cliente.
3. O retorno do endpoint deve ser um JSON com a chave **`type`**, contendo a classificação da pergunta.

### Objetivo

A avaliação será focada no **processo de validação das perguntas** e na implementação do código em Python. Além disso, será fornecida uma lista com exemplos de perguntas e as classificações corretas para ajudar na criação do seu prompt.

Embora não seja possível criar um prompt 100% assertivo, você pode incluir observações sobre possíveis melhorias no processo de validação.
