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


## Exigência de código 2 de 7

```python
   class VehicleRegistrationHashTable:
    def __init__(self):
        self.table = [None] * 10
```

- Essa classe representa a tabela Hash com um atributo.
- **Tabela**: Um vetor de 10 posições, onde cada posição é uma lista encadeada de estados.
- Inicialmente todas posições são **None**

### Em resumo:

- Está criando a base da tabela hash com 10 "gavetas", são onde os estados serão inseridos, podendo formar listas ligadas em caso de colisão.


## Exigência de código 3 de 7

```python
def state_code_hash_calculate_function(self, state_code):
        if state_code == 'DF':
            return 7
        else:
            return (ord(state_code[0]) + ord(state_code[1])) % 10
```

- Esta função é responsável por converter a sigla denim estado em um índice numérico (de 0 a 9) na tabela hash.
- "DF" Retorna 7 ( regra especifica)
- **Outros estados**: Soma os valores numéricos dos dois primeiros caracteres da sigla e aplica o módulo 10 (% 10). Isso garante que o resultado seja sempre uma posição válida na tabela.

## Exigência de código 4 de 7

```python
  def insert_state(self, state_name, state_code):
        index = self.state_code_hash_calculate_function(state_code)
        new_state = State(state_name, state_code)
        if not self.table[index]:
            self.table[index] = new_state
        else:
            new_state.next = self.table[index]
            self.table[index] = new_state

```

- Esta função é responsável por adicionar um novo estado à sua VehicleRegistrationHashTable. Ela lida tanto com a inserção simples quanto com o caso de colisão, usando a técnica de endereçamento em cadeia (listas encadeadas).
- Calcula o índice de onde o estado deve ir usando a função hash.
- Cria um novo objeto State.
- Verifica a posição:
   * Se a posição na tabela estiver vazia, o novo estado é inserido diretamente lá.
   * Se a posição já tiver um estado (colisão), o novo estado é adicionado no início da lista encadeada daquela posição, tornando-se o primeiro elemento.
 
## Exigência de Código 5 de 7

```python
    def print_table(self):
        for i in range(10):
            print(f'Index {i}: ', end='')
            current = self.table[i]
            while current:
                print(f'{current.state_code} -> ', end='')
                current = current.next
            print('None')
```

- A função print_table mostra o conteúdo da sua tabela hash.
Ela percorre as 10 posições da tabela:
 * Para cada posição, imprime o índice.
 * Em seguida, percorre e imprime as siglas dos estados encadeados nessa posição, usando -> para indicar a ligação.
 * Termina cada linha com None, mostrando o fim da lista encadeada.


## Exigência de código 6 de 7

```python
def main():
    hash_table = VehicleRegistrationHashTable()

    # Exigência de saída de console 1 de 3
    print("\n--- Tabela Hash antes de inserir qualquer estado ---")
    hash_table.print_table()

    # Lista completa dos 26 estados + DF
    brazilian_states = [
        ('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'),
        ('Bahia', 'BA'), ('Ceará', 'CE'), ('Distrito Federal', 'DF'),
        ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'),
        ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'),
        ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'),
        ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'),
        ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'),
        ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'),
        ('Tocantins', 'TO')
    ]

    # Inserção dos estados
    for state_name_brazilian, state_code_brazilian in brazilian_states:
        hash_table.insert_state(state_name_brazilian, state_code_brazilian)
```


- Configuração Inicial e População de Dados
- Esta parte do código é a função principal (main) que demonstra o uso da VehicleRegistrationHashTable.
- Ela realiza as seguintes ações:

   * Inicializa a tabela hash vazia.
   * Imprime o estado inicial da tabela (vazia).
   * Define uma lista com todos os estados brasileiros e o Distrito Federal.
   * Insere cada um desses estados na tabela hash, utilizando a lógica de inserção já implementada.

