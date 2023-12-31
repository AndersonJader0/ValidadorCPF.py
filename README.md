# Validador de CPF desenvolvido em Python

## Descrição do Projeto (/◕ヮ◕)/
### 🎯Desenvolvido com o intuito de ser utilizado em Projetos reais por qualquer pessoa (^-^)/

### Sobre o código (◕‿◕)
- Possui apenas 74 linhas.
- Organizado em Classes e Métodos
- Faz reuso dos métodos
- Importado somente os módulos `sys` e `re`
- Possui um método especial `manipulador()` responsável por orquestrar todo o funcionamento
- Funciona com CPFs que possuem traços e pontos
- Valida se possui os 11 digitos do CPF e se são números
- Aponta para o usuário qualquer caracter especial diferente de - ou . utilizado

### Fluxograma do Validador
![image](https://github.com/AndersonJader0/ValidadorCPF.py/assets/105549520/1bc0a566-b4f6-4c8c-84be-bfff7a9a3fe5)

### Algoritmo para validação de Cadastro de Pessoas Físicas (CPF) realiza os seguintes calculos aritméticos: (︶^︶)

- Para o primeiro dígito verificador:
- `1 - Multiplicação dos 9 primeiros dígitos do CPF por 10, 9, 8... 2`
- `2 - A soma de todas as multiplicações`
- `3 - Calculo do resto da soma`
- `4 - Se o resto da soma for igual a 0 ou 1 então o digito verificador é igual a 0 se for diferente disso será o resultado da subtração por 11`
- `5 - Validação do resultado obtido dos calculos com o *primeiro* dígito verificador do CPF`
- Para o segundo dígito verificador:
- `1 - Multiplicação dos 10 primeiros dígitos do CPF por 11, 10, 9... 2`
- `2 - A soma de todas as multiplicações`
- `3 - Calculo do resto da soma`
- `4 - Se o resto da soma for igual a 0 ou 1 então o digito verificador é igual a 0 se for diferente disso será o resultado da subtração por 11`
- `5 - Validação do resultado obtido dos calculos com o *segundo* dígito verificador do CPF`

##### O digito 1 e Digito 2 correspondem ao Verificador 1 e Verificador 2

### Projeto aberto para quaisquer melhorias ( ˃̵ᴗ˂̵)ﻭ
