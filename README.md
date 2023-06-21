
# Random Line from File

Este script em Python lê um arquivo de texto e imprime uma linha aleatória do arquivo.
(Se em cada linha só tiver uma palavra ele imprime uma palavra aleatória do arquivo. Se cada linha tiver uma frase, ele imprime uma frase aleatória.)

## Pré-requisitos

- Python 3.x

## Utilização

1. Execute o script em um ambiente Python.
2. Será solicitado que você forneça o nome do arquivo, incluindo a extensão.
3. O script verificará se o arquivo existe.
4. Será impressa uma linha aleatória do arquivo.

## Exemplo

Suponha que temos um arquivo chamado "example.txt" com o seguinte conteúdo:

```
Hello, world!
This is an example file.
Random Line from File script.
Have a nice day!
```

Ao executar o script e fornecer o nome do arquivo "example.txt", ele selecionará uma linha aleatória do arquivo e a imprimirá. Por exemplo:

```
$ python random_line_from_file.py example.txt
This is an example file.
```

Neste exemplo, a linha "This is an example file." foi selecionada aleatoriamente do arquivo "example.txt" e exibida na saída.

## Observação

Certifique-se de fornecer o nome do arquivo corretamente, incluindo a extensão. O arquivo deve existir no diretório em que o script está sendo executado.

