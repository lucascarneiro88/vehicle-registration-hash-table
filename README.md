# Sistema de Emplacamento de Veículos com Tabela Hash

## Visão Geral

Este repositório contém um projeto em Python desenvolvido como parte de uma tarefa da faculdade, com foco em estruturas de dados, mais especificamente na implementação de uma **Tabela Hash com endereçamento em cadeia**.

## Enunciado

Com o objetivo de criar um novo sistema de emplacamento de veículos, deputados do **Distrito Federal – DF** decidiram que o **último número da placa dos veículos** irá representar o **estado de registro** do veículo.

Para isso, sua equipe de desenvolvedores foi encarregada de desenvolver uma **Tabela Hash com endereçamento em cadeia** de **10 posições** (cada posição do vetor deve ser uma lista encadeada), representando os números de 0 a 9 que servirão como "índices" para os **26 estados e o Distrito Federal** (total de 27).

---

## Exigência de código 1 de 7

Implementar uma **Tabela Hash com 10 posições**, onde inicialmente **todas as posições possuem valor `None`**.
### Exigência de código 1 de 7

Implementar uma **Tabela Hash com 10 posições**, onde inicialmente **todas as posições possuem valor `None`**.

#### Exemplo de implementação da estrutura de estado:

```python
class States:
    def __init__(self, state_name, state_code):
        self.state_name = state_name 
        self.state_code = state_code  
        self.current = None           
```


- Esta classe representa um estado , com três atributos:


  **state_code** (sigla): Representa a sigla do estado, por exemplo 'RS' para Rio Grande do Sul.

  **state_name** (nome_do_estado): Nome completo do estado, como 'Rio Grande do Sul'.

  **current** (próximo): Um ponteiro para o próximo estado na lista encadeada. Inicialmente, este valor é None.

### Observação sobre None:
No Python, None é um valor especial que representa a ausência de valor — semelhante ao null em outras linguagens de programação.
Neste contexto, significa que o estado atual (ex: RS) ainda não aponta para nenhum próximo estado na lista encadeada.

Isto é importante porque se esta criando uma lista encadeada. Onde cada estado pode apontar para outro estado na tabela hash(em caso de colisão).
    Mas no momento em que o objeto é criado, ele ainda não tem nenhum próximo, por isso começa com:

```python

    self.proximo = None
```

- Depois que o valor mudar um novo estado é inserido e há colisão, esse atributo "proximo" passa a apontar para outro 
"estado" da mesma lista.

ex: 
   RJ --> SP --> MG --> None

### Em Resumo:
- self.proximo = None, serve para inicializar a ligação vazia, e só depois ela é usada para apontar para outro "estado", caso haja colisões na tabela hash.
