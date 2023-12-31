# Validador de CPF desenvolvido em Python

## Descrição do Projeto (/◕ヮ◕)/
### Algoritmo para validação de Cadastro de Pessoas Físicas (CPF) realiza os seguintes calculos aritméticos: (︶^︶)

- Para o primeiro dígito verificador:
- `1 - Multiplicação dos 9 primeiros dígitos do CPF por 10, 9, 8 sucessivamente`
- `2 - A soma de todas as multiplicações`
- `3 - Calculo do resto da soma`
- `4 - Se o resto da soma for igual a 0 ou 1 então o digito verificador é igual a 0 se for diferente disso será o resultado da subtração por 11`
- `5 - Validação do resultado obtido dos calculos com o *primeiro* dígito verificador do CPF`
- Para o segundo dígito verificador:
- `1 - Multiplicação dos 10 primeiros dígitos do CPF por 11, 10, 9 sucessivametne`
- `2 - A soma de todas as multiplicações`
- `3 - Calculo do resto da soma`
- `4 - Se o resto da soma for igual a 0 ou 1 então o digito verificador é igual a 0 se for diferente disso será o resultado da subtração por 11`
- `5 - Validação do resultado obtido dos calculos com o *segundo* dígito verificador do CPF`
