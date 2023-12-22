# InstaZap

O **InstaZap** é um projeto que visa criar uma interface simples para gerar um link para o WhatsApp sem a necessidade de anotar o número da pessoa. Desenvolvido usando a biblioteca **Flet**, o projeto proporciona uma experiência amigável e fácil de usar.

## Funcionalidades

- **Gerar Link para WhatsApp:** Insira o número de telefone desejado e clique no botão "Gerar Link" para obter um link direto para o WhatsApp com o número fornecido.

- **Copiar Link:** Após gerar o link, clique no botão "Copiar Link" para copiá-lo para a área de transferência, facilitando o compartilhamento.

- **Validação de Número:** O projeto inclui uma verificação básica para garantir que o número de telefone inserido seja válido.

## Como Executar

Certifique-se de ter Python instalado em seu ambiente. Você pode rodar o projeto executando o script Python:

```bash
python InstaZap.py
```

## Dependências

O projeto utiliza as seguintes bibliotecas Python:

- **Flet:** Uma biblioteca para criar interfaces gráficas de usuário simples e interativas.
- **Pyperclip:** Utilizado para manipulação da área de transferência, facilitando a cópia de links gerados.

Instale as dependências utilizando o seguinte comando:

```bash
pip install flet pyperclip
