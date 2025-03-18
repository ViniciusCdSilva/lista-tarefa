class listarefa:
    def __init__(self):
        self.tarefas=[]

    def add_tarefas(self,tarefa):
        self.tarefas.append({"tarefa":tarefa,"status": "pendente"})
        print(f"Tarefa{tarefa}adicionada com sucesso!")

    def list_tarefas(self):
        if not self.tarefas :
            print("nenhuma tarefa cadastrada")
            return
        print("Listas de tarefas")
        for n, tarefa in enumerate(self.tarefas , start=1):
            status = tarefa["status"]
            print(f"{n}.{tarefa['tarefa']}-{status}")

    def conc_tarefa(self,indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice - 1]["status"]="Concluída"
            print(f"Tarefa{self.tarefas[indice - 1]['tarefas']} concluída com sucesso!")





def menu():
    lista = listarefa()
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
            lista.add_tarefas(tarefa)
            print ("\n Adicionar tarefa ")

        elif opcao == "2":
            lista.list_tarefas()

        elif opcao=="3":
            try:
                indice =int(input("Digite o numero de tarefas que desja concluir: "))
                lista.conc_tarefa(indice)
            except ValueError:
                print("Digite um numero valido ")       
        
menu()        
        