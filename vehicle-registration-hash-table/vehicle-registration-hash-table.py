# Exigência de código 1 de 7
# Classe que representa um Estado
class State:
    def __init__(self, state_name, state_code):
        self.state_name = state_name
        self.state_code = state_code
        self.next = None


# Exigência de código 2 de 7
# Classe para a tabela hash
class VehicleRegistrationHashTable:
    def __init__(self):
        self.table = [None] * 10

    # Exigência de código 3 de 7
    # Função para calcular a posição do índice na tabela hash
    def state_code_hash_calculate_function(self, state_code):
        if state_code == 'DF':
            return 7
        else:
            return (ord(state_code[0]) + ord(state_code[1])) % 10

    # Exigência de código 4 de 7
    # Função para inserir o estado na tabela hash
    def insert_state(self, state_name, state_code):
        index = self.state_code_hash_calculate_function(state_code)
        new_state = State(state_name, state_code)
        if not self.table[index]:
            self.table[index] = new_state
        else:
            new_state.next = self.table[index]
            self.table[index] = new_state

    # Exigência de código 5 de 7
    # Função para imprimir a tabela hash
    def print_table(self):
        for i in range(10):
            print(f'Index {i}: ', end='')
            current = self.table[i]
            while current:
                print(f'{current.state_code} -> ', end='')
                current = current.next
            print('None')


# Exigência de código 6 de 7
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

    # Exigência de saída de console 2 de 3
    print("\n--- Tabela Hash após inserir os 26 estados + DF ---")
    hash_table.print_table()

    # Exigência de código 7 de 7
    fictitious_state_name = "Lucas Carneiro"
    fictitious_state_code = "LC"
    hash_table.insert_state(fictitious_state_name, fictitious_state_code)

    # Exigência de saída de console 3 de 3
    print("\n--- Tabela Hash após inserir o estado fictício ---")
    hash_table.print_table()


if __name__ == "__main__":
    main()
