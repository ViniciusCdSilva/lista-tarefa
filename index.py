class listarefa:
    def __init__(self):
        self.tarefa =[]

    def add_tarefas(self,tarefa):
        self.tarefa.append({"tarefa":tarefa,"status": "pendente"})
        print(f"Tarefa{tarefa}adicionada com sucesso!")




def menu():
    while True :
        print("Menu")
        print("\n 1. Adicionar tarefa")
        print("\n 2. Listar tarefas")
        print("\n 3. Concluir tarefa")
        print("\n 4. Remover tarefa")
        print("\n 5. Sair")

        opcao = input("Escolha uma opção :")

        if opcao == "1":
            tarefa = input("Digite a sua tarefa")
            lista.add_tarefa(tarefa)
            print ("\n Adicionar tarefa ")
        
menu()        
        