# Palhoburger - Sistema de Pedidos de Lanches

![Palhoburger Logo](logo.png)

Este é o projeto final desenvolvido para a disciplina de Desenvolvimento Desktop. O aplicativo Palhoburger é um sistema de pedidos para o lanche Palhoburger. Ele foi construído utilizando a framework QTDesigner para o desenvolvimento das interfaces do aplicativo.

## Funcionalidades

O aplicativo Palhoburger possui duas telas principais:

### Tela 1 - Lista de Pedidos

Na tela 1, o cliente tem acesso às seguintes informações:

- **Nome do Lanche**: Exibe o nome do lanche, Palhoburger, para identificação.
- **Novo Pedido**: Permite ao cliente iniciar um novo pedido, acessando a tela 2.
- **Pedidos Realizados**: Exibe uma tabela com os pedidos já realizados, contendo informações como número do pedido, nome do cliente e status.

### Tela 2 - Realizar Pedido

Na tela 2, o cliente pode realizar um novo pedido, fornecendo as seguintes informações:

- **Nome do Cliente**: Campo de texto para inserir o nome do cliente.
- **Hambúrguer**: Caixa de seleção para escolher o tipo de hambúrguer desejado.
- **Refrigerante**: Caixa de seleção para escolher o tipo de refrigerante desejado.
- **Acompanhamento**: Caixa de seleção para escolher o tipo de acompanhamento desejado.
- **Quantidade**: Caixa de seleção para selecionar a quantidade desejada.
- **Cadastrar**: Botão para cadastrar o pedido, salvando-o no banco de dados e retornando à Tela 1.
- **Voltar**: Botão para voltar à Tela 1 sem cadastrar o pedido.

Ao cadastrar um novo pedido, ele será salvo no banco de dados e aparecerá na lista de pedidos realizados da Tela 1. O cliente pode selecionar um pedido na lista para visualizar suas informações, sendo redirecionado para a Tela 2. Na Tela 2, é possível alterar o pedido, voltar à Tela 1 ou excluir o pedido.

## Requisitos do Sistema

- Sistema operacional: Ubuntu, Windows ou macOS
- Python 3.x
- QTDesigner
- Bibliotecas Python: PyQt5, SQLAlchemy

## Instalação

1. Clone este repositório em sua máquina:

```
git clone https://github.com/MatheusAmarall/ProjetoFinalDesktop.git
```

2. Certifique-se de ter o Python 3.x instalado em sua máquina.

3. Instale as bibliotecas necessárias utilizando o seguinte comando:

```
pip install PyQt5 SQLAlchemy
```

4. Execute o aplicativo utilizando o seguinte comando:

```
python main.py
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma "issue" neste repositório.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
*Aviso: O Palhoburger é um projeto fictício criado apenas para fins educacionais no âmbito da disciplina de Desenvolvimento Desktop.*
